from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class BibleSection(Base):
    __tablename__ = 'section'

    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'))
    section = relationship(BibleSection)


class Chapter(Base):
    __tablename__ = "chapter"
    id = Column(Integer, primary_key=True)
    chapter = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'))
    book = relationship(Book)


class Verse(Base):
    __tablename__ = "verse"

    id = Column(Integer, primary_key=True)
    verse_number = Column(String(10), nullable=False)
    verse_string = Column(String(1000), nullable=False)
    chapter_id = Column(Integer, ForeignKey('chapter.id'))
    chapter = relationship(Chapter)


class Years(Base):
    __tablename__ = 'years'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, nullable=False)


engine = create_engine(database='sqlite:///bibledatabase.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

if __name__ == '__main__':
    pass
