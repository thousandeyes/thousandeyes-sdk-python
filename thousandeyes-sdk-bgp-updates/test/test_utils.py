# coding: utf-8

import json
import unittest
from typing import Any

from pydantic import BaseModel


def _project_onto_constructed(expected: Any, constructed: Any) -> Any:
    """Keep only example fields that appear in the constructed model output."""
    if isinstance(constructed, dict):
        if not isinstance(expected, dict):
            return expected
        return {
            key: _project_onto_constructed(expected.get(key), value)
            for key, value in constructed.items()
        }
    if isinstance(constructed, list):
        if not isinstance(expected, list):
            return expected
        return [
            _project_onto_constructed(expected[index], value)
            for index, value in enumerate(constructed)
        ]
    return expected


def assert_constructed_model_matches_example_json(model: BaseModel, loaded_json: dict):
    test_case = unittest.TestCase()
    test_case.maxDiff = None
    test_case.assertIsNotNone(model)
    constructed_json = json.loads(model.to_json())
    projected_loaded_json = _project_onto_constructed(loaded_json, constructed_json)
    sorted_loaded_json = json.dumps(projected_loaded_json, sort_keys=True)
    sorted_constructed_json = json.dumps(constructed_json, sort_keys=True)
    test_case.assertEqual(sorted_loaded_json, sorted_constructed_json)
