import json


class Store:
    def __init__(self, file_name):
        self.file_name = file_name

        self._create_file()

    def _create_file(self):
        f = open(self.file_name, "w+")
        f.close()

    def save(self, tweets):
        with open(self.file_name, 'w') as f:
            json.dump(tweets, f)

    def list(self):
        with open(self.file_name) as f:
            return json.load(f)