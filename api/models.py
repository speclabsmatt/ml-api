from sqlalchemy import Column, Integer, Text
from .database import Base
import re


class Entry(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    data = Column(Text)

    def __init__(self, data):
        self.data = data
        # self.title = title
        # self.summary = summary
        # self.slug = re.sub('[^\w]+', '_', self.title.lower())

    def __repr__(self):
        return '<Entry %r>' % self.data
