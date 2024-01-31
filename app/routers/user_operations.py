from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, schemas, models
from .auth import get_current_user

router = APIRouter(tags=['User Operations'])

@router.get("/users/me/", response_model=schemas.UserOut)
async def read_users_me(current_user: schemas.UserOut = Depends(get_current_user), db: Session = Depends(database.get_db)):
    # Assuming get_current_user dependency ensures authentication,
    # returns the current user based on the token provided.
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")