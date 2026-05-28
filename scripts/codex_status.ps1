param(
  [string]$Root = (Resolve-Path ".").Path
)

$dev = Join-Path $Root "docs/development.md"
if (!(Test-Path $dev)) {
  throw "No existe docs/development.md"
}

$content = Get-Content -Path $dev
$start = ($content | Select-String -Pattern "^## Estado de progreso del MVP" | Select-Object -First 1).LineNumber
$next = ($content | Select-String -Pattern "^## Plan de trabajo por fases" | Select-Object -First 1).LineNumber

if ($start -and $next) {
  $content[($start - 1)..($next - 2)]
} else {
  Select-String -Path $dev -Pattern "Progreso global estimado|Tarea pendiente|Siguiente paso"
}
