from pydantic import BaseModel


class AddCommentReqDto(BaseModel):

    comment: str

class AddCommentResDto(AddCommentReqDto):
    id: int