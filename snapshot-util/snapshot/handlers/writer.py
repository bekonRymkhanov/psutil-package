import json

class SnapshotWriter:
    """Handles writing snapshots to a file."""

    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        """Writes snapshot data to file."""
        with open(self.filename, "a") as file:
            json.dump(data, file)
            file.write("\n")
