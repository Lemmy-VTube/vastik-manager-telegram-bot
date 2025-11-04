from dataclasses import dataclass
from datetime import datetime
from logging import getLogger
from typing import Optional

import aiohttp

from src.config import config

logger = getLogger(__name__)


@dataclass
class Schedule:
    photo_id: str
    message_streamer_text: str
    updated_at: datetime


class ScheduleService:
    def __init__(self) -> None:
        self.base_url: str = config.BACKEND_URL.get_secret_value()
    
    async def get_schedule(self) -> Optional[Schedule]:
        url = f"{self.base_url}/schedule"
        logger.debug(f"Requesting schedule from backend: {url}")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        logger.warning(f"Backend returned {response.status} for schedule {id}")
                        return None

                    data = await response.json()
                    logger.debug(f"Response data: {data}")
                    schedule_data = data.get("data")
                    if not schedule_data:
                        logger.debug("No schedule data found in response")
                        return None

                    updated_at = datetime.fromisoformat(schedule_data["updated_at"])
                    schedule = Schedule(
                        photo_id=schedule_data["photo_id"],
                        message_streamer_text=schedule_data["message_streamer_text"],
                        updated_at=updated_at,
                    )
                    logger.debug(f"Schedule parsed successfully: {schedule}")
                    return schedule
        except aiohttp.ClientError as e:
            logger.error(f"Network error while fetching schedule: {e}")
            return None
        except Exception as e:
            logger.exception(f"Unexpected error while getting schedule: {e}")
            return None


schedule_service = ScheduleService()
