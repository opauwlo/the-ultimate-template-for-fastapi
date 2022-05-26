
from fastapi import APIRouter, Depends, HTTPException
from .user_service import UserService
from .dto.create_user_dto import CreateUserDto
from .dto.update_user_dto import UpdateUserDto

router = APIRouter()   

@router.get("/get_all",
    response_model=list,
    summary="Get all users",
    description="Get all users",
    status_code=200
)
async def get_all_users():
    return UserService.get_all_users()

@router.post("/store",
    response_model=CreateUserDto,
    summary="Store user",
    description="Store user",
    status_code=201
)
async def store_user(data: CreateUserDto):
    try:
        return UserService.store_user(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/update",
    response_model=UpdateUserDto,
    summary="Update user",
    description="Update user",
    status_code=201
)
async def update_user(data: UpdateUserDto):
    return UserService.update_user(data)