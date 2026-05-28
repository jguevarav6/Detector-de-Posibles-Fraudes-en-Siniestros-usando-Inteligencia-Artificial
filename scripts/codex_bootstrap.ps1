param(
  [string]$ProjectRoot = (Resolve-Path ".").Path,
  [string]$CodexHome = "$env:USERPROFILE\.codex"
)

$source = Join-Path $ProjectRoot ".codex\skills"
$target = Join-Path $CodexHome "skills"

if (!(Test-Path $source)) {
  throw "No existe carpeta de skills del proyecto: $source"
}

New-Item -ItemType Directory -Force -Path $target | Out-Null

Get-ChildItem -Path $source -Directory | ForEach-Object {
  $destination = Join-Path $target $_.Name
  if (Test-Path $destination) {
    Remove-Item -LiteralPath $destination -Recurse -Force
  }
  Copy-Item -LiteralPath $_.FullName -Destination $destination -Recurse
  Write-Output "Instalado skill: $($_.Name)"
}

Write-Output "Skills FraudLens instalados en $target"
Write-Output "En nuevas sesiones, menciona el skill por nombre o trabaja dentro del repo con .codex/fraudlens.yml como manifiesto."
