from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from eme.entities import loadConfig

config = loadConfig("core/content/ctx.ini")
db_type = config['db']['type']

if db_type == 'postgres':
    # an Engine, which the Session will use for connection
    # resources
    some_engine = create_engine('{type}+psycopg2://{user}:{password}@{host}/{database}'.format(**config[db_type]))
elif db_type == 'sqlite':
    some_engine = create_engine('sqlite:///{file}'.format(**config[db_type]), connect_args={'check_same_thread': False})
else:
    raise Exception("Wrong db_type used in database config {}".format(db_type))

Session = sessionmaker(bind=some_engine)

session = Session()


def get_session(force=False):
    if force:
        session.close()


    return session
