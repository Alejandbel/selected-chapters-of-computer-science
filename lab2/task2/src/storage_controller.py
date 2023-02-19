import re

from storage_service import StorageService


class StorageController:
    _storage_service = StorageService()

    @staticmethod
    def _split_keys_and_apply_function(keys: str, function: callable):
        for key in keys.split():
            function(key)

    def add(self, args: str):
        if not args:
            print('Nothing to add')
            return

        self._split_keys_and_apply_function(args, self._storage_service.add)
        print('Successfully added keys to storage')

    def _remove_key(self, key: str):
        if self._storage_service.find(key):
            self._storage_service.remove(key)
        else:
            print(f'Cant remove key {key}. It does not exists')

    def remove(self, args: str):
        if not args:
            print('Nothing to remove')
            return

        self._split_keys_and_apply_function(args, self._remove_key)

    def list(self, args):
        print(' '.join(self._storage_service.list()))

    def find(self, args: str):
        if not args:
            print('Nothing to find')
            return

        self._split_keys_and_apply_function(
            args,
            lambda key: print(f'Key {key} {"" if self._storage_service.find(key) else "not "}exists')
        )

    def grep(self, args):
        if not args:
            print('Empty regexp')
            return

        try:
            regexp = re.compile(args)
        except re.error:
            print('Incorrect regexp')
            return

        keys_found = self._storage_service.grep(regexp)

        if not keys_found:
            print('No such elements')
            return

        print(' '.join(keys_found))

    def save(self):
        pass

    def load(self):
        pass
