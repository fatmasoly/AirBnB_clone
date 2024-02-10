#!/usr/bin/python3
"""This module for unittests for models/file_storage.py."""

import unittest
from unittest.mock import patch, mock_open, MagicMock
from models.engine.file_storage import FileStorage
from models.user import User


