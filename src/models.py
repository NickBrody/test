from typing import Dict, Any

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql+psycopg2://admin:admin@db:5432/admin")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Freelancer(Base):
    __tablename__ = 'freelancer'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(200), nullable=False)
    experience = Column(String(200))
    contacts = Column(String(100))


    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(200), nullable=False)
    experience = Column(String(200))
    contacts = Column(String(100))


    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}
