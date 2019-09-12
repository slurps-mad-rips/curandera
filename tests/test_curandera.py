from curandera import __version__
from curandera.tool import CMake
from pathlib import Path


def test_version():
    assert __version__ == "0.1.0"


def test_cmake_binary():
    cmake = CMake()
    assert cmake.binary == Path.cwd() / "build"


def test_cmake_source():
    cmake = CMake()
    assert cmake.source == Path.cwd()
