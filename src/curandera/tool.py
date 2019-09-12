from dataclasses import dataclass, field
from functools import partial
from pathlib import Path

import subprocess
import shutil
import os

import cmake as upstream


def current(*args) -> Path:
    return Path.cwd().joinpath(*args)


@dataclass(init=False, frozen=True)
class CTest:
    prg: Path = field(default=Path(shutil.which("ctest", path=upstream.CMAKE_BIN_DIR)))


@dataclass(init=False, frozen=True)
class CPack:
    prg: Path = field(default=Path(shutil.which("cpack", path=upstream.CMAKE_BIN_DIR)))


@dataclass(frozen=True)
class CMake:
    prg: Path = field(init=False, default=Path(shutil.which("cmake", path=upstream.CMAKE_BIN_DIR)))

    src: Path = field(default_factory=current)
    dst: Path = field(default_factory=partial(current, "build"))

    @property
    def binary(self) -> Path:
        return self.dst

    @property
    def source(self) -> Path:
        return self.src

    @property
    def binary_dir(self) -> str:
        return os.fspath(self.binary)

    @property
    def source_dir(self) -> str:
        return os.fspath(self.src)

    @property
    def program(self) -> str:
        return os.fspath(self.prg)

    @property
    def generator(self) -> str:
        return "Ninja"

    @property
    def api(self) -> Path:
        return Path(self.binary_dir) / ".cmake" / "api" / "v1"

    def configure(self):
        args = [
            self.program,
            f"-B{self.binary_dir}",
            f"-S{self.source_dir}",
            f"-G{self.generator}",
        ]
        process = subprocess.run(args, capture_output=True, check=True)
        print(process.stdout, process.stderr)

    def build(self):
        args = [self.program, "--build", f"{self.binary_dir}"]
        process = subprocess.run(args, capture_output=True, check=True)
        print(process.stdout, process.stderr)
