import random

from sqlalchemy.orm import Session

from .utils import schema_exists
from .users import seed_users


def seed_all(session: Session):
    random.seed(0)

    seed_users(session)
