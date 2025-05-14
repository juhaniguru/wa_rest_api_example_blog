from fastapi import Depends
from sqlalchemy.orm import Session

import models
from custom_exceptions.blog import BlogAppNotFoundError
from db import init_db
from dtos.blog import AddBlogReqDto


class CommentSrv:
    def __init__(self, db: Session):
        self.db = db

    def get_all_by_blog(self, blog_id: int):
        return self.db.query(models.Comments).filter(models.Comments.blogs_id == blog_id).all()

    def get_by_id(self, comment_id: int):
        comment = self.db.query(models.Comments).filter(models.Comments.id == comment_id).first()
        if comment is None:
            raise BlogAppNotFoundError()
        return comment

    def remove_by_id(self, comment_id: int):
        item = self.get_by_id(comment_id)
        self.db.delete(item)
        self.db.commit()

    def add(self, data: AddBlogReqDto, blog_id: int) -> models.Comments:
        comment = models.Comments(**data.model_dump())
        comment.blogs_id = blog_id
        self.db.add(comment)
        self.db.commit()
        return comment

    def update(self, data: AddBlogReqDto, blog_id: int, comment_id: int) -> models.Comments:
        comment = self.get_by_id(comment_id)
        comment.comment = data.comment
        self.db.commit()
        return comment

    def get_comment(self, blog_id: int, comment_id: int):
        comment = self.db.query(models.Comments).filter(models.Comments.blogs_id == blog_id).filter(
            models.Comments.id == comment_id).first()
        if comment is None:
            raise BlogAppNotFoundError()
        return comment


def init_comment_service(db: Session = Depends(init_db)):
    return CommentSrv(db)
