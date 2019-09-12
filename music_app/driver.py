import click
import json

from parser import (
    Parser,
    READ_DB,
    READ_CHANGES,
)
from change import commit_changes


def convert_to_dict(obj):
    """
    A function takes in a custom object and returns a dictionary representation of the object.
    """
    return obj.__dict__

class MusicAppDriver:
    def __init__(self):
        self.parser = Parser()

    def execute(self, sourcefile, changesfile, outputfile):

        if not (sourcefile and changesfile and outputfile):
            # ideally initialize a default DB or changes doc
            return

        self.database = self.parser.read_from_file(sourcefile, READ_DB)
        self.changes = self.parser.read_from_file(changesfile, READ_CHANGES)
        commit_changes(self.database, self.changes)

        with open(outputfile , 'w') as outfile:
            json.dump(
                self.database,
                outfile,
                default=convert_to_dict,
                indent=4,
            )



@click.command()
@click.option("--sfl", help="Source file location")
@click.option("--cfl", help="Change file location")
@click.option("--ofl", help="Output file location")
def music_driver(sfl,cfl,ofl):
    MusicAppDriver().execute(sfl,cfl,ofl)

if __name__ == '__main__':
    music_driver()