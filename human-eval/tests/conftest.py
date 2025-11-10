# tests/conftest.py
import sys
from pathlib import Path

# Ensure repo root is first on sys.path so "gemini_cot", "gpt_sp", etc. are importable
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))
