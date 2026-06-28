"""
create_ai.py

Creates the Bootstrap AI subsystem.

Run:
    python create_ai.py
"""

from pathlib import Path

ROOT = Path("bootstrap") / "ai"

folders = [
    ROOT,
    ROOT / "agents",
    ROOT / "memory",
    ROOT / "models",
    ROOT / "orchestration",
    ROOT / "prompts",
    ROOT / "providers",
    ROOT / "reasoning",
    ROOT / "tools",
]

files = {
    ROOT / "__init__.py": '"""Bootstrap AI."""\n',
    ROOT / "README.md": "# Bootstrap AI\n\nThe intelligence subsystem.\n",

    ROOT / "agents" / "__init__.py": "",
    ROOT / "agents" / "architect.py": '"""Architect Agent."""\n',
    ROOT / "agents" / "builder.py": '"""Builder Agent."""\n',
    ROOT / "agents" / "engineer.py": '"""Engineer Agent."""\n',
    ROOT / "agents" / "planner.py": '"""Planner Agent."""\n',
    ROOT / "agents" / "researcher.py": '"""Researcher Agent."""\n',
    ROOT / "agents" / "reviewer.py": '"""Reviewer Agent."""\n',
    ROOT / "agents" / "supervisor.py": '"""Supervisor Agent."""\n',

    ROOT / "memory" / "__init__.py": "",
    ROOT / "memory" / "context.py": '"""Context memory."""\n',
    ROOT / "memory" / "embeddings.py": '"""Embeddings."""\n',
    ROOT / "memory" / "repository.py": '"""Repository memory."""\n',
    ROOT / "memory" / "sessions.py": '"""Session memory."""\n',

    ROOT / "models" / "__init__.py": "",
    ROOT / "models" / "agent.py": '"""Agent model."""\n',
    ROOT / "models" / "response.py": '"""Response model."""\n',
    ROOT / "models" / "task.py": '"""Task model."""\n',

    ROOT / "orchestration" / "__init__.py": "",
    ROOT / "orchestration" / "coordinator.py": '"""Coordinator."""\n',
    ROOT / "orchestration" / "pipeline.py": '"""AI pipeline."""\n',
    ROOT / "orchestration" / "task_queue.py": '"""Task queue."""\n',
    ROOT / "orchestration" / "workflow.py": '"""Workflow."""\n',

    ROOT / "prompts" / "architect.md": "# Architect Prompt\n",
    ROOT / "prompts" / "engineer.md": "# Engineer Prompt\n",
    ROOT / "prompts" / "reviewer.md": "# Reviewer Prompt\n",
    ROOT / "prompts" / "researcher.md": "# Researcher Prompt\n",

    ROOT / "providers" / "__init__.py": "",
    ROOT / "providers" / "openai.py": '"""OpenAI provider."""\n',
    ROOT / "providers" / "anthropic.py": '"""Anthropic provider."""\n',
    ROOT / "providers" / "ollama.py": '"""Ollama provider."""\n',
    ROOT / "providers" / "lmstudio.py": '"""LM Studio provider."""\n',

    ROOT / "reasoning" / "__init__.py": "",
    ROOT / "reasoning" / "planner.py": '"""Reasoning planner."""\n',
    ROOT / "reasoning" / "critic.py": '"""Critic."""\n',
    ROOT / "reasoning" / "reflection.py": '"""Reflection."""\n',
    ROOT / "reasoning" / "evaluator.py": '"""Evaluator."""\n',

    ROOT / "tools" / "__init__.py": "",
    ROOT / "tools" / "engineering.py": '"""Engineering tools."""\n',
    ROOT / "tools" / "filesystem.py": '"""Filesystem tools."""\n',
    ROOT / "tools" / "git.py": '"""Git tools."""\n',
    ROOT / "tools" / "plugins.py": '"""Plugin tools."""\n',
    ROOT / "tools" / "terminal.py": '"""Terminal tools."""\n',
    ROOT / "tools" / "web.py": '"""Web tools."""\n',
}

print("="*60)
print(" Bootstrap AI Scaffolder")
print("="*60)

created = 0

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

for path, content in files.items():
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"✓ Created {path}")
        created += 1
    else:
        print(f"• Exists   {path}")

print("-"*60)
print(f"Files created: {created}")
print("Bootstrap AI subsystem ready.")
