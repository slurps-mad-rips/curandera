from dataclasses import dataclass


@dataclass(order=True)
class Version:
    major: int
    minor: int
