'''
Handles commiting operations related to changes file
'''
def commit_changes(database, change):
    # throw exception if database or change is empty based on use case

    if not (change or database):
        return

    add_change(change.add, database)
    delete_change(change.delete, database)
    update_change(change.update, database)


def add_change(change, database):
    # if needed we can return true or false to denote success or failure
    if not (change and database):
        return

    for user in (change.users or []):
        database.add_user(user)

    for playlist in (change.playlists or []):
        database.add_playlist(playlist)

def delete_change(change, database):
    # if needed we can return true or false to denote success or failure
    if not (change and database):
        return

    for user in (change.users or []):
        database.delete_user(user)

    for playlist in (change.playlists or []):
        database.delete_playlist(playlist)

    # if needed we can do for delete songs as well

def update_change(change, database):
    # if needed we can return true or false to denote success or failure
    if not (change and database):
        return

    for user in (change.users or []):
        database.update_user(user)

    for playlist in (change.playlists or []):
        database.update_playlist(playlist)

    # if needed we can do for update songs as well