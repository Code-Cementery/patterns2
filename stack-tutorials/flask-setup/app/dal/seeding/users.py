import bcrypt
from sqlalchemy.orm import Session

from ..entities.user import User


def seed_users(session: Session):
    pw = bcrypt.hashpw("hotmail".encode('utf-8'), bcrypt.gensalt())
    salt = bcrypt.gensalt()

    test_user = User(username="oboforty", password=pw, salt=salt)

    session.add(test_user)
