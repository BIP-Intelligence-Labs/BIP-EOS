"""M-006.7.4 Prompt Engine (Starter)"""
class PromptEngine:
    def render(self, template: str, **kwargs) -> str:
        return template.format(**kwargs)
