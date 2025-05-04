from typing import Annotated, List

from fastapi import APIRouter, Path
from starlette.exceptions import HTTPException
from starlette.responses import Response

from custom_exceptions.blog import BlogAppNotFoundError
from dependencies import BlogService, CommentService
from dtos.blog import GetBlogResDto, AddBlogResDto, AddBlogReqDto
from dtos.comment import AddCommentReqDto, AddCommentResDto

router = APIRouter(tags=["blogs"], prefix="/api/v1/blogs")


@router.get("/")
def get_blogs(service: BlogService) -> List[GetBlogResDto]:
    return service.get_all()


@router.get("/{blog_id}")
def get_blog(service: BlogService, blog_id: int = Path(gt=0)) -> GetBlogResDto:
    try:
        return service.get_by_id(blog_id)
    except BlogAppNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{blog_id}")
def delete_blog(service: BlogService, blog_id: int = Path(gt=0)):
    try:
        service.remove_by_id(blog_id)
        return Response(status_code=204)
    except BlogAppNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
def add_blog(service: BlogService, req_data: AddBlogReqDto) -> AddBlogResDto:
    return service.add(req_data)


@router.get("/{blog_id}/comments")
async def get_comments(service: CommentService,
                       blog_id: int = Path(gt=0)) -> List[AddCommentResDto]:
    return service.get_all_by_blog(blog_id)


@router.post("/{blog_id}/comments")
async def add_comment(req_data: AddCommentReqDto, service: CommentService,
                      blog_id: int = Path(gt=0)) -> AddCommentResDto:
    return service.add(req_data, blog_id=blog_id)


@router.put("/{blog_id}/comments/{comment_id}")
async def add_comment(req_data: AddCommentReqDto, service: CommentService,
                      blog_id: int = Path(gt=0), comment_id: int = Path(gt=0)) -> AddCommentResDto:
    return service.update(req_data, blog_id, comment_id)


@router.delete("/{blog_id}/comments/{comment_id}")
def delete_blog(service: CommentService, blog_id: int = Path(gt=0), comment_id: int = Path(gt=0)):
    try:
        service.remove_by_id(comment_id)
        return Response(status_code=204)
    except BlogAppNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
