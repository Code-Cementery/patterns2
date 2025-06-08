from dal import get_session, User


class UserRepository:

    def find_by(self, username) -> User:
        with get_session() as session:
            return session.query(User)\
                .filter(User.username == username)\
                .first()

    def get(self, uid) -> User:
        with get_session() as session:
            return session.get(User, uid)
