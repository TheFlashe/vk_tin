import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import UniqueConstraint

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, unique=True, nullable=False)  # ID в ВК
    first_name = sq.Column(sq.String(50), nullable=False)
    last_name = sq.Column(sq.String(50), nullable=False)
    profile = relationship("Profile", back_populates="user", uselist=False)
    photos = relationship("Photo", back_populates="user")


class Profile(Base):
    __tablename__ = "profiles"

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("users.id"), nullable=False)
    gender = sq.Column(sq.String(10), nullable=False)  # 'male'/'female'/'other'
    age = sq.Column(sq.Integer, nullable=False)
    city = sq.Column(sq.String(50), nullable=False)
    user = relationship("User", back_populates="profile")


class Photo(Base):
    __tablename__ = "photos"

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("users.id"), nullable=False)
    url = sq.Column(sq.Text, nullable=False)
    likes_count = sq.Column(sq.Integer, default=0)  # Критерий популярности
    user = relationship("User", back_populates="photos")


class Favorite(Base):
    __tablename__ = "favorites"
    __table_args__ = (
        UniqueConstraint('user_id', 'favorite_vk_id', name='unique_favorite'),
    )

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey("users.id"), nullable=False)
    favorite_vk_id = sq.Column(sq.Integer, nullable=False)  # ID избранного в ВК


def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
