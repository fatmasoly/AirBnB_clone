#!/usr/bin/python3
"""A script to instantiate and reload the FileStorage object."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
