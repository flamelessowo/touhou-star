from abc import ABC, abstractmethod


class GobjAbs(ABC):
    @abstractmethod
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
