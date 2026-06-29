class Plugin:
    name = "reports"
    version = "0.1.0"

    def load(self):
        print(f"Loading {self.name} plugin")

    def capabilities(self):
        return [
            "pdf_export",
            "docx_export",
            "html_export",
        ]
