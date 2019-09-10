class JsonSerializer:

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class User(JsonSerializer):

    def __init__(self, id, name=None):
        self.id = id
        self.name = name

    def update(self, other):
        if other.name:
            self.name = other.name


class Playlist(JsonSerializer):

    def __init__(self, id, user_id=None, song_ids=None):
        self.id = id
        self.user_id = user_id
        self.song_ids = song_ids

    def update(self, other_playlist):
        # given use case is just for addition of songs. No deletion is present
        # for now.

        if not other_playlist.song_ids:
            raise Exception("Songs in playlist is empty")

        # if needed check if song exist in the system or not

        self.song_ids.extend(
            other_playlist.song_ids
        )

class Song(JsonSerializer):

    def __init__(self, id, artist=None, title=None):
        self.id = id
        self.artist = artist
        self.title = title

    def update(self, other):

        if other.artist:
            self.artist = other.artist

        if other.title:
            self.title = other.title


class MusicDb(object):

    def __init__(self, users, playlists, songs):
        self.users = users
        self.playlists = playlists
        self.songs = songs

    @classmethod
    def from_json(cls, data):
        users = list(map(User.from_json, data.get("users", [])))
        playlists = list(map(Playlist.from_json, data.get("playlists", [])))
        songs = list(map(Song.from_json, data.get("songs", [])))
        return cls(users, playlists, songs)

    def add_user(self, user):
        # if needed check if duplicate exist, throw exception or replace
        # based on usecase
        self.users.append(user)

    def is_user_exist(self, id):
        users = [
            user for user in self.users if user.id == id
        ]
        return len(users) > 0


    def delete_user(self, user_to_del):
        self.users = [
            user for user in self.users if user.id != user_to_del.id
        ]

    def update_user(self, user_to_update):
        for user in self.users:
            if user.id == user_to_update.id:
                user.update(user_to_update)


    def add_playlist(self, playlist):
        # if needed check if duplicate exist, throw exception or replace
        # based on usecase
        if not self.is_user_exist(playlist.user_id):
            raise Exception("user id do not exist")

        if not (playlist.song_ids or len(playlist.song_ids)):
            raise Exception("Song list is empty")

        self.playlists.append(playlist)

    def delete_playlist(self, playlist_to_del):
        self.playlists = [
            playlist for playlist in self.playlists if playlist.id != playlist_to_del.id
        ]

    def update_playlist(self, other_playlist):
        for playlists in self.playlists:
            if playlists.id == other_playlist.id:
                playlists.update(other_playlist)


class Changes:

    def __init__(self, add, delete, update):
        self.add = add
        self.delete = delete
        self.update = update

    @classmethod
    def from_json(cls, data):
        add_list = map(MusicDb.from_json, data.get("add", {}))
        db_add = None
        if len(add_list):
            db_add = add_list[0]

        db_delete = None
        delete_list = map(MusicDb.from_json, data.get("delete", {}))
        if len(delete_list):
            db_delete = delete_list[0]

        db_update = None
        update_list = map(MusicDb.from_json, data.get("update", {}))
        if len(update_list):
            db_update = update_list[0]

        return cls(db_add, db_delete, db_update)

