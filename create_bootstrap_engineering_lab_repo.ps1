# create_bootstrap_engineering_lab_repo.ps1
# Requires GitHub CLI (gh): https://cli.github.com/

$RepoName = "bootstrap-engineering-lab"
$Visibility = "public"   # Change to "private" if desired

Write-Host ""
Write-Host "========================================"
Write-Host " Bootstrap Engineering Lab Repository"
Write-Host "========================================"
Write-Host ""

# Verify GitHub CLI
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "GitHub CLI (gh) is not installed."
    Write-Host "Install it from https://cli.github.com/"
    exit 1
}

# Authenticate if needed
gh auth status *> $null
if ($LASTEXITCODE -ne 0) {
    gh auth login
}

# Create repository
gh repo create $RepoName --$Visibility --description "Bootstrap Engineering Factory Kernel and Plugins" --source . --remote origin --push

Write-Host ""
Write-Host "Repository created successfully!"
Write-Host ""

git remote -v
git status
