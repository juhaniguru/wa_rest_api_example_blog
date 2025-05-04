from fastapi import Depends
from sqlalchemy.orm import Session

import models
from custom_exceptions.blog import BlogAppNotFoundError
from db import init_db
from dtos.blog import AddBlogReqDto


class BlogsSrv:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(models.Blogs).all()

    def get_by_id(self, blog_id: int):
        blog = self.db.query(models.Blogs).filter(models.Blogs.id == blog_id).first()
        if blog is None:
            raise BlogAppNotFoundError()
        return blog

    def remove_by_id(self, blog_id: int):
        blog = self.get_by_id(blog_id)
        for comment in blog.comments:
            self.db.delete(comment)
        self.db.delete(blog)
        self.db.commit()

    def add(self, data: AddBlogReqDto) -> models.Blogs:
        blog = models.Blogs(**data.model_dump())
        self.db.add(blog)
        self.db.commit()
        return blog


def init_blog_service(db: Session = Depends(init_db)):
    return BlogsSrv(db)
