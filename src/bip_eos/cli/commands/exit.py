from bip_eos.cli.command import Command


class ExitCommand(Command):

    name = "exit"

    description = "Exit UEOS."

    aliases = ["quit"]

    def execute(self, args: list[str]) -> int:

        print("Shutting down UEOS...")

        raise SystemExit(0)
