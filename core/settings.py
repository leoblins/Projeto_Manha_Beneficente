import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Define qual config será usada
if os.getenv("RENDER", "") == "TRUE":
    from .settings_prod import *
else:
    from .settings_local import *
