param(
  [string]$Root = (Resolve-Path ".").Path
)

$files = @(
  "docs/arquitectura.md",
  "docs/development.md",
  ".codex/fraudlens.yml",
  "FraudLens_Claims_AI_Plan_HackIAthon.md",
  "Proyecto.md"
)

foreach ($file in $files) {
  $path = Join-Path $Root $file
  if (Test-Path $path) {
    Write-Output "===== $file ====="
    Get-Content -Path $path -TotalCount 80
    Write-Output ""
  }
}
