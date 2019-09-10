from unittest import TestCase
from music_app.parser import (
    Parser,
    READ_DB,
    READ_CHANGES
)

class TestParser(TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_read_from_file_changes(self):
        changes = self.parser.read_from_file("add_user_changes.json", READ_CHANGES)
