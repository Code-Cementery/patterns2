import uuid

from sqlalchemy import Column, String, Boolean, SmallInteger, TIMESTAMP, func, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import Column

from ..base import Base


class User(Base):
    __tablename__ = "users"

    uid = Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    username: str = Column("username", String(32), nullable=False, unique=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

    salt = Column(LargeBinary(60), nullable=True)
    password = Column(LargeBinary(60))
    admin = Column(Boolean(), default=False)

    @property
    def view(self):
        # view by default has no face

        return {
            "uid": self.uid,
            "username": self.username,
            "admin": self.admin,
            "points": self.points,
        }

    def get_id(self):
        return str(self.uid) if self.uid else None

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.uid is not None

    @property
    def is_anonymous(self):
        return False

    def get_user_id(self):
        # used for oauth2
        return self.uid

    def __hash__(self):
        return hash(self.uid)

    def __repr__(self):
        return "{}({}..)".format(self.username, str(self.uid)[0:4])
