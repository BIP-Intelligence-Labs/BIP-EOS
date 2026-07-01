from __future__ import annotations

from bip_eos.cli.command import Command
from bip_eos.cli.dispatcher import CommandDispatcher


class HelpCommand(Command):

    name = "help"

    description = "Show available commands."

    aliases = ["?"]

    def __init__(self, dispatcher: CommandDispatcher):

        self.dispatcher = dispatcher

    def execute(self, args: list[str]) -> int:

        print()

        print("Available Commands\n")

        for command in self.dispatcher.commands():

            print(f"{command.name:<15}{command.description}")

        print()

        return 0
