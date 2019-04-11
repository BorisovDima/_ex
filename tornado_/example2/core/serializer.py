class SimpleSerializer:
    serialize_fields = []

    # def serialize(self):
    #     columns = self.__mapper__.relationships.keys()
    #     rel = self.__table__.columns.keys()
    #     data = []
    #     for f in self.serialize_fields:
    #         if f in columns:
    #             field = getattr(self, f)
    #         elif f in rel:
    #             field = []
    #             for r in getattr(self, f)[:20]:
    #                 field.append()


