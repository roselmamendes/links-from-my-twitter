from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    tweet_id = Column(String(250), nullable=False)


class Store:
    def __init__(self, database_name):
        self.database_name = database_name

        self._set_database()

    def _set_database(self):
        engine = create_engine(f'sqlite:///{self.database_name}.db')

        Base.metadata.create_all(engine)

        Base.metadata.bind = engine

        DBSession = sessionmaker(bind=engine)

        self.session = DBSession()

    def save(self, tweet):
        new_url_db = Url(
            url=tweet.expanded_url,
            created_at=tweet.created_at,
            tweet_id=tweet.id_str
        )
        self.session.add(new_url_db)
        self.session.commit()

    def list(self):
        urls = self.session.query(Url).all()
        return urls