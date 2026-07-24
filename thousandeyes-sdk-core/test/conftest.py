import sys
from pathlib import Path

_core_test_support = Path(__file__).resolve().parent
if str(_core_test_support) not in sys.path:
    sys.path.insert(0, str(_core_test_support))
