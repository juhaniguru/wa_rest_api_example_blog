from typing import Annotated

from fastapi import Depends

from services.blogs import BlogsSrv, init_blog_service
from services.comments import CommentSrv, init_comment_service

BlogService = Annotated[BlogsSrv, Depends(init_blog_service)]
CommentService = Annotated[CommentSrv, Depends(init_comment_service)]