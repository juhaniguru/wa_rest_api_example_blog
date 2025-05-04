from typing import List, Optional

from sqlalchemy import Column, ForeignKeyConstraint, Index, String, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        Index('username_UNIQUE', 'username', unique=True),
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    username = mapped_column(String(45), nullable=False)
    password = mapped_column(String(255), nullable=False)

    blogs: Mapped[List['Blogs']] = relationship('Blogs', uselist=True, back_populates='users')
    comments: Mapped[List['Comments']] = relationship('Comments', uselist=True, back_populates='users')


class Blogs(Base):
    __tablename__ = 'blogs'
    __table_args__ = (
        ForeignKeyConstraint(['users_id'], ['users.id'], name='fk_blogs_users1'),
        Index('fk_blogs_users1_idx', 'users_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    name = mapped_column(String(255), nullable=False)
    body = mapped_column(Text, nullable=False)
    users_id = mapped_column(INTEGER(11))

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='blogs')
    comments: Mapped[List['Comments']] = relationship('Comments', uselist=True, back_populates='blogs')


class Comments(Base):
    __tablename__ = 'comments'
    __table_args__ = (
        ForeignKeyConstraint(['blogs_id'], ['blogs.id'], name='fk_comments_blogs'),
        ForeignKeyConstraint(['users_id'], ['users.id'], name='fk_comments_users1'),
        Index('fk_comments_blogs_idx', 'blogs_id'),
        Index('fk_comments_users1_idx', 'users_id')
    )

    id = mapped_column(INTEGER(11), primary_key=True)
    comment = mapped_column(Text, nullable=False)
    blogs_id = mapped_column(INTEGER(11), nullable=False)
    users_id = mapped_column(INTEGER(11))

    blogs: Mapped['Blogs'] = relationship('Blogs', back_populates='comments')
    users: Mapped[Optional['Users']] = relationship('Users', back_populates='comments')
