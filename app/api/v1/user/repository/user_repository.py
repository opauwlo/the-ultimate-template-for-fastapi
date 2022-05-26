from ..dto.create_user_dto import CreateUserDto
from ..dto.update_user_dto import UpdateUserDto

class UserRepository:
    def get_all_users():
        return [
            {
                "id": 1,
                "username": "test",
                "avatar_url": "https://avatars0.githubusercontent.com/u/1234?v=4",
                "avatar_id": "1234",
                "bio": "test"
            }
        ]

    def store_user(data: CreateUserDto):
        return data

    def update_user(data: UpdateUserDto):
        return data