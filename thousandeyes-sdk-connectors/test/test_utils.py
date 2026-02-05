# coding: utf-8

import json
import unittest

from pydantic import BaseModel


def assert_constructed_model_matches_example_json(model: BaseModel, loaded_json: dict):
    test_case = unittest.TestCase()
    test_case.maxDiff = None
    test_case.assertIsNotNone(model)
    constructed_json = json.loads(model.to_json())
    sorted_loaded_json = json.dumps(loaded_json, sort_keys=True)
    sorted_constructed_json = json.dumps(constructed_json, sort_keys=True)
    test_case.assertEqual(sorted_loaded_json, sorted_constructed_json)
