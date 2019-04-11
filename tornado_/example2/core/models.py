from tornado_sqlalchemy import declarative_base

from sqlalchemy import Integer, Column, DateTime, String
from datetime import datetime
from .serializer import Serializer
from tornado_sqlalchemy import as_future

Base = declarative_base()

class BaseChatModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    date_create = Column(DateTime, default=datetime.utcnow)

    def serialize(self, to_json=False):
        raise NotImplementedError

    async def save(self, session):
        session.add(self)
        try:
            await as_future(session.commit)
        except Exception:
            pass

def Media(count):

    class Meta:
        def __init_subclass__(cls, **kwargs):
            for i in range(count):
                setattr(cls, f'media{ i or str()}', Column(String(124)))

    class MediaModel(Meta):
        pass

    return MediaModel