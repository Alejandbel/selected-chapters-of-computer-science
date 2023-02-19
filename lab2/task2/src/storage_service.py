import re


class StorageService:
    _storage: set[str] = set()

    def add(self, key: str):
        self._storage.add(key)

    def remove(self, key: str):
        self._storage.remove(key)

    def list(self):
        return list(self._storage)

    def find(self, key):
        return key in self._storage

    def grep(self, regex):
        return list(filter(lambda key: re.match(regex, key), self._storage))

    def save(self):
        pass

    def load(self):
        pass
