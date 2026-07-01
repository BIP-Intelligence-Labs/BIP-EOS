from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):

    name: str = ""

    description: str = ""

    aliases: list[str] = []

    @abstractmethod
    def execute(self, args: list[str]) -> int:
        """
        Execute the command.

        Return:
            0 = success
            non-zero = error
        """
        raise NotImplementedError
