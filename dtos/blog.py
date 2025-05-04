from pydantic import BaseModel


class GetBlogResDto(BaseModel):
    id: int
    name: str
    body: str


class AddBlogReqDto(BaseModel):
    name: str
    body: str


class AddBlogResDto(AddBlogReqDto):
    id: int
