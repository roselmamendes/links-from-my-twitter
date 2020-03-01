import json
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Bookmark(Base):
    __tablename__ = 'bookmark'

    id = Column(Integer, primary_key=True)
    created_at = Column(String(250), nullable=False)
    source_id = Column(String(250), nullable=False)
    source = Column(String(250), nullable=False)
    source_fields = Column(String(250), nullable=False)
    urls = relationship('Url')


class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    bookmark_id = Column(Integer, ForeignKey('bookmark.id'))


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

    def save(self, bookmark):
        new_bookmark_db = Bookmark(
            created_at=bookmark.created_at,
            source_id=bookmark.source_id,
            source=bookmark.source,
            source_fields=json.dumps(bookmark.source_fields)
        )
        self.session.add(new_bookmark_db)
        self.session.commit()

        for url in bookmark.urls:
            new_url = Url(url=url, bookmark_id=new_bookmark_db.id)
            self.session.add(new_url)
            self.session.commit()

    def list(self):
        bookmarks = self.session.query(Bookmark).all()
        return bookmarks