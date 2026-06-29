from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINEERING = ROOT / 'engineering'

DIRECTORIES = {
    'philosophy': [
        'EP-001-engineering-philosophy.md',
        'EP-002-domain-first-engineering.md',
        'EP-003-architecture-before-implementation.md',
        'EP-004-engineering-as-a-product.md',
        'README.md',
    ],
    'metamodel': [
        'EM-001-engineering-specification.metamodel.yaml',
        'EM-002-domain-manifest.metamodel.yaml',
        'EM-003-builder-domain.metamodel.yaml',
        'README.md',
    ],
    'architecture': [
        'BA-001-builder-architecture.md',
        'BA-002-domain-contract.md',
        'BA-003-domain-lifecycle.md',
        'BA-004-domain-manifest.md',
        'BA-005-bootstrap-engine.md',
        'README.md',
    ],
    'standards': [
        'ES-001-engineering-specification-standard.md',
        'ES-002-documentation-standard.md',
        'ES-003-coding-standard.md',
        'ES-004-testing-standard.md',
        'README.md',
    ],
    'domains': [
        'DM-001-builder-domain.md',
        'DM-002-lead-domain.md',
        'README.md',
    ],
    'adr': [],
    'governance': [],
    'reference': [],
    'milestones': [],
    'sprints': [],
}

def banner():
    print('=' * 70)
    print('BIP EOS Engineering Knowledge System Bootstrap')
    print('=' * 70)

def create_file(path: Path):
    if path.exists():
        print(f'[SKIP] {path}')
        return False
    path.write_text('', encoding='utf-8')
    print(f'[FILE] {path}')
    return True

def main():
    banner()
    ENGINEERING.mkdir(exist_ok=True)
    created_dirs = created_files = skipped_files = 0
    for directory, files in DIRECTORIES.items():
        folder = ENGINEERING / directory
        if not folder.exists():
            folder.mkdir(parents=True)
            created_dirs += 1
            print(f'[DIR ] {folder}')
        for f in files:
            if create_file(folder / f):
                created_files += 1
            else:
                skipped_files += 1
    print('-' * 70)
    print(f'Directories : {created_dirs}')
    print(f'Files Created: {created_files}')
    print(f'Files Skipped: {skipped_files}')
    print('=' * 70)
    print('Engineering Knowledge System ready.')

if __name__ == '__main__':
    main()
