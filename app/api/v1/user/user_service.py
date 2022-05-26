from .dto.create_user_dto import CreateUserDto
from .dto.update_user_dto import UpdateUserDto
from .repository.user_repository import UserRepository

class UserService:
        
        def get_all_users():
            return UserRepository.get_all_users()
    
        def store_user(data: CreateUserDto):
            return UserRepository.store_user(data)

        def update_user(data: UpdateUserDto):
            return UserRepository.update_user(data)