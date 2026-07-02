from pathlib import Path
r=Path('reports');r.mkdir(exist_ok=True)
(r/'import_migration_report.md').write_text('# Import Migration Report\n')
