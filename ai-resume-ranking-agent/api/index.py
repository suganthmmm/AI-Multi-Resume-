import sys
import os
from pathlib import Path

# Add the project root to sys.path so we can import 'main' and 'app' packages
root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(root_path))

from app.main import app
