from app import db

class BaseModel(db.Model):
    __abstract__ = True

    date_created = db.Column(db.DateTime, index=True)
    id = db.Column(db.Integer, primary_key=True)

    def _commit(self):
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)

    def save(self):
        db.session.add(self)
        self._commit()

    def delete(self):
        db.session.remove(self)
        self._commit()