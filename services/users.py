from typing import Annotated

from fastapi.params import Depends
from sqlalchemy.orm import Session

from db import init_db


class UsersSrv:
    def __init__(self, db: Session):
        self.db = db


def init_users_service(db: Session = Depends(init_db)):
    return UsersSrv(db)

UsersService = Annotated[UsersSrv,Depends(init_users_service)]