"""Entrypoint para Streamlit Community Cloud.

Streamlit Cloud usa por defecto `streamlit_app.py` como main file path.
Este wrapper invoca el router principal en src/app/main.py y evita el
auto-discovery de carpetas pages/.

Local:
    streamlit run streamlit_app.py
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.app.main import main  # noqa: E402

main()
