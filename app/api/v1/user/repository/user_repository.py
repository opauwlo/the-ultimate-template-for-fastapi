from ..dto.create_user_dto import CreateUserDto
from ..dto.update_user_dto import UpdateUserDto
from app.database.models import User



class UserRepository:
    def get_all_users():
        return User.query.all()

    def store_user(data: CreateUserDto):
        return data

    def update_user(data: UpdateUserDto):
        return data