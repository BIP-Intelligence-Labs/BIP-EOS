"""
UEOS Interactive Shell

M-006.2
"""

from __future__ import annotations

from ueos.cli.dispatcher import CommandDispatcher


class Shell:
    """
    Interactive UEOS shell.
    """

    def __init__(self, dispatcher: CommandDispatcher) -> None:
        self.dispatcher = dispatcher

    def run(self) -> None:
        """
        Start the interactive shell.
        """

        while True:

            try:

                line = input("UEOS> ").strip()

                if not line:
                    continue

                self.dispatcher.dispatch(line)

            except KeyboardInterrupt:

                print("\nUse 'exit' to quit.")

            except EOFError:

                print()
                break

            except SystemExit:

                break

            except Exception as ex:

                print(f"ERROR: {ex}")
