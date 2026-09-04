import sys
from pathlib import Path

_repo_root = Path(__file__).resolve().parents[2]
_core_test_support = _repo_root / "thousandeyes-sdk-core" / "test"
if str(_core_test_support) not in sys.path:
    sys.path.insert(0, str(_core_test_support))
