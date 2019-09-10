from unittest import TestCase
from music_app.parser import (
    Parser,
    READ_DB,
    READ_CHANGES
)
from music_app.change import commit_changes

class TestCommit_changes(TestCase):

    def setUp(self):
        self.parser = Parser()
        self.database = self.parser.read_from_file("mixtape-data.json",
            READ_DB)

    def test_commit_changes_user_add(self):
        changes = self.parser.read_from_file("add_user_changes.json", READ_CHANGES)
        self.assertEqual(len(self.database.users), 7)

        commit_changes(self.database, changes)
        self.assertEqual(len(self.database.users), 8)


    def test_commit_changes_user_delete(self):
        changes = self.parser.read_from_file(
            "delete_user_changes.json", READ_CHANGES
        )
        self.assertEqual(len(self.database.users), 7)

        commit_changes(self.database, changes)
        self.assertEqual(len(self.database.users), 6)


    def test_commit_changes_user_update(self):
        changes = self.parser.read_from_file(
            "update_user_changes.json", READ_CHANGES
        )
        self.assertEqual(self.database.users[-1].name, "Seyyit Nedim")

        commit_changes(self.database, changes)
        self.assertEqual(self.database.users[-1].name, "Seyyit")

    def test_commit_changes_playlist_update_add_song(self):
        changes = self.parser.read_from_file("update_playlist.json", READ_CHANGES)
        self.assertEqual(len(self.database.playlists[0].song_ids), 2)

        commit_changes(self.database, changes)
        self.assertEqual(len(self.database.playlists[0].song_ids), 3)

    def test_commit_changes_playlist_add_playlist(self):
        changes = self.parser.read_from_file("add_playlist.json", READ_CHANGES)
        self.assertEqual(len(self.database.playlists), 3)

        commit_changes(self.database, changes)
        self.assertEqual(len(self.database.playlists), 4)

    def test_commit_changes_playlist_delete_playlist(self):
        changes = self.parser.read_from_file(
            "delete_playlist.json", READ_CHANGES)
        self.assertEqual(len(self.database.playlists), 3)

        commit_changes(self.database, changes)
        self.assertEqual(len(self.database.playlists), 2)

    def test_commit_changes_playlist_invalid_playlist(self):
        changes = self.parser.read_from_file(
            "invalid_playlist.json", READ_CHANGES)

        with self.assertRaises(Exception):
            commit_changes(self.database, changes)