from logging import getLogger
from typing import Optional

import aiohttp

from src.config import config
from src.schemas import ScheduleRead

logger = getLogger(__name__)


class ScheduleService:
    def __init__(self) -> None:
        self.base_url: str = config.BACKEND_URL.get_secret_value()

    async def get_schedule(self) -> Optional[ScheduleRead]:
        url = f"{self.base_url}/v1/schedule"
        logger.debug(f"Requesting schedule from backend: {url}")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    status = response.status
                    logger.debug(f"Response status: {status}")

                    if status != 200:
                        logger.warning(f"Backend returned {status} while fetching schedule.")
                        return None

                    data = await response.json()
                    logger.debug(f"Raw response data: {data}")

                    schedule_data = data.get("data", {}).get("schedule")
                    if not schedule_data:
                        logger.debug("Schedule is empty or null in backend response.")
                        return None

                    try:
                        schedule = ScheduleRead(**schedule_data)
                        logger.debug(f"Schedule parsed successfully: {schedule}")
                        return schedule
                    except Exception as e:
                        logger.exception(f"Error while parsing schedule data: {e}")
                        return None
        except aiohttp.ClientError as e:
            logger.error(f"Network error while fetching schedule: {e}")
            return None
        except Exception as e:
            logger.exception(f"Unexpected error while getting schedule: {e}")
            return None


schedule_service = ScheduleService()
