from sqlalchemy import func, desc
from sqlalchemy.orm import Session

from core.entities import User


class UserRepository():

    def __init__(self, db_session):
        self.session: Session = db_session


    def get(self, uid=None, email=None, username=None, code=None):

        if uid is not None:
            user = self.session.query(User).get(uid)
        elif username is not None:
            user = self.session.query(User).filter(User.username == username).first()
        elif email is not None:
            user = self.session.query(User).filter(User.email == email).first()
        elif code is not None:
            user = self.session.query(User).filter(User.forgot_code == code).first()
        else:
            user = None

        return user

    def delete(self, user: User):
        self.session.delete(user)
        self.session.commit()

    def create(self, user: User):
        self.session.add(user)
        self.session.commit()

    def save(self, user: User):
        self.session.add(user)
        self.session.commit()

    def save_world(self, user: User):
        self.session.query(User).update({User.wid: user.wid, User.iso: user.iso})
        self.session.commit()

