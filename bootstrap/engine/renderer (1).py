"""
bootstrap/engine/renderer.py

UEOS BFS-002
Template Renderer
"""

from __future__ import annotations

from string import Template
from typing import Any


class TemplateRenderer:
    """
    Renders UEOS templates using Python's standard Template engine.
    """

    def render(self, template_text: str, context: dict[str, Any]) -> str:
        return Template(template_text).safe_substitute(context)

    def render_from_loader(self, loader, template_name: str, context: dict[str, Any]) -> str:
        template = loader.load(template_name)
        return self.render(template, context)


if __name__ == "__main__":
    renderer = TemplateRenderer()

    template = """
# ${title}

Author: ${author}
Version: ${version}
"""

    output = renderer.render(
        template,
        {
            "title": "UEOS",
            "author": "Engineering Team",
            "version": "1.0",
        },
    )

    print("=" * 72)
    print("UEOS Template Renderer")
    print("=" * 72)
    print(output)
