param([string]$Root = (Resolve-Path ".").Path)
$required = @("docs/arquitectura.md", "docs/development.md", "FraudLens_Claims_AI_Plan_HackIAthon.md", "Proyecto.md")
foreach ($file in $required) {
  $path = Join-Path $Root $file
  if (!(Test-Path $path)) { throw "Falta contexto requerido: $file" }
}
Write-Output "Contexto FraudLens disponible para architect."
