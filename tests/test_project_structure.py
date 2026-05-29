"""Pruebas de estructura minima del proyecto."""

from pathlib import Path


def test_required_docs_and_presentation_exist() -> None:
    required = [
        "README.md",
        "docs/arquitectura.md",
        "docs/uso_ia.md",
        "docs/reglas_negocio.md",
        "docs/etica_privacidad.md",
        "docs/limitaciones.md",
        "docs/demo_script.md",
        "presentation/pitch.md",
    ]

    for path in required:
        assert Path(path).exists(), path
