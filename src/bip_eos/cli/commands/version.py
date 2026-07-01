from bip_eos.cli.command import Command


class VersionCommand(Command):

    name = "version"

    description = "Display UEOS version."

    aliases = ["ver"]

    def execute(self, args: list[str]) -> int:

        print("UEOS 0.1.0 Genesis")

        return 0
