from logging import getLogger
from typing import List, Optional

import aiohttp

from src.config import config
from src.schemas import UserCreate, UserRead

logger = getLogger(__name__)


class UserService:
    def __init__(self) -> None:
        self.base_url: str = config.BACKEND_URL.get_secret_value()

    async def create_user(self, user_data: UserCreate) -> Optional[UserRead]:
        url = f"{self.base_url}/v1/users/create"
        payload = user_data.model_dump(mode="json")

        logger.debug(f"Sending user creation request → {url}")
        logger.debug(f"Payload: {payload}")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload) as response:
                    data = await response.json()
                    logger.debug(f"Response ({response.status}): {data}")

                    if response.status != 200:
                        logger.warning(
                            f"Failed to create user {user_data.tg_id}, status={response.status}"
                        )
                        return None

                    user_info = data.get("data", {}).get("user")
                    if not user_info:
                        logger.warning("No 'user' field in response.")
                        return None
                    try:
                        user = UserRead(**user_info)
                        logger.debug(
                            f"User created successfully: tg_id={user.tg_id}, id={user.id}"
                        )
                        return user
                    except Exception as e:
                        logger.exception(f"Error parsing user data: {e}")
                        return None
        except aiohttp.ClientError as e:
            logger.error(f"Network error during user creation: {e}")
            return None
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            return None

    async def get_all_users(self, limit: int = 100, offset: int = 0) -> Optional[List[UserRead]]:
        url = f"{self.base_url}/v1/users?limit={limit}&offset={offset}"
        logger.debug(f"Fetching all users from {url}")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    logger.debug(f"Response ({response.status}): {data}")

                    if response.status != 200:
                        logger.warning(f"Failed to fetch users, status={response.status}")
                        return None

                    users_data = data.get("data", {}).get("users")
                    if not users_data:
                        logger.debug("No users found in backend response.")
                        return []

                    users: List[UserRead] = []
                    for user_info in users_data:
                        try:
                            users.append(UserRead(**user_info))
                        except Exception as e:
                            logger.warning(f"Skipping invalid user entry: {e}")
                    logger.debug(f"Successfully parsed {len(users)} users")
                    return users
        except aiohttp.ClientError as e:
            logger.error(f"Network error while fetching users: {e}")
        except Exception as e:
            logger.exception(f"Unexpected error while getting users: {e}")
        return None


user_service = UserService()
