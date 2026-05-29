"""Entrypoint Streamlit en la raiz del proyecto.

Uso:
    streamlit run app.py

Este wrapper evita que Streamlit auto-detecte carpetas pages/ y mantiene
un unico router controlado en src/app/main.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.app.main import main  # noqa: E402

if __name__ == "__main__":
    main()
else:
    main()
