#!/usr/bin/python3
"""Module for from_json_string(my_str)"""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
