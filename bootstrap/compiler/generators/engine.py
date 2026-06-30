from pathlib import Path

class SpecificationGenerator:

    def __init__(self, specification, title, content):
        self.specification = specification
        self.title = title
        self.content = content

    @property
    def target(self):
        return (
            Path.cwd()
            / "engineering"
            / "compiler"
            / "specifications"
            / f"{self.specification}.md"
        )

    def generate(self, overwrite=False):
        print("=" * 60)
        print("BIP EOS Bootstrap")
        print("=" * 60)
        print(f"Specification : {self.title}")
        print()

        self.target.parent.mkdir(parents=True, exist_ok=True)

        if self.target.exists() and not overwrite:
            print("Status        : Already Exists")
        else:
            self.target.write_text(self.content.strip() + "\n", encoding="utf-8")
            print("Status        : Created")

        print(f"Location      : {self.target}")
