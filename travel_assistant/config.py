"""Configuración compartida por todos los agentes."""

import os

from dotenv import load_dotenv

load_dotenv(override=True)

MODEL = os.getenv("TRAVEL_MODEL", "gemini-3.5-flash-lite")

# Poner USE_GOOGLE_SEARCH=true en el .env si la cuenta tiene Google Search habilitado.
USE_GOOGLE_SEARCH = os.getenv("USE_GOOGLE_SEARCH", "false").strip().lower() == "true"
