class BaseSerializer:

    def __getitem__(self, item):
        return getattr(self, item)