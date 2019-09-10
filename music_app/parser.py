import json
from user import (
    MusicDb,
    Changes
)
READ_DB = "read_db"
READ_CHANGES = "read_changes"

class Parser:

    def read_from_file(self, filename, action):

        if not (filename or action):
            # ideally initialize a default DB or changes doc
            return

        with open(filename) as f:
            data = json.load(f)
            if action == READ_DB:
                data_base = MusicDb.from_json(data)
            elif action == READ_CHANGES:
                data_base = Changes.from_json(data)
            return data_base