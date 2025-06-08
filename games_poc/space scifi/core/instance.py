from core.dal.ctx import session
from core.dal.repositories import UserRepository


users = UserRepository(db_session=session)
