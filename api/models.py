from sqlalchemy import Column, Integer, Text
from .database import Base
import re


class Entry(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text)

    def __init__(self, content):
        self.content = content
        # self.title = title
        # self.summary = summary
        # self.slug = re.sub('[^\w]+', '_', self.title.lower())

    def __repr__(self):
        return '<Entry %r>' % self.content
