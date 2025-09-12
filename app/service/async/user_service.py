from typing import Optional
from datetime import date
from app.repo.asyncs.user_repo import AsyncUserRepo, AsyncTargetRepo
from app.models.user_model import UserBase, UserTargetBase
from app.shemas.report_shema import RangeReport, DailyReport


class AsyncUserService:
    def __init__(self):
        self.user_repo = AsyncUserRepo()
        self.user_daily_repo = AsyncTargetRepo()

    async def get(self, id: int) -> Optional[UserBase]:
        user = await self.user_repo.get(id)
        return user

    async def get_by_tg_id(self, tg_id: int) -> Optional[UserBase]:
        user = await self.user_repo.get_by_tg_id(tg_id)
        return user

    async def create(self, user: UserBase) -> UserBase:
        user = await self.user_repo.create(user)
        return user

    async def update(self, user: UserBase) -> Optional[UserBase]:
        user = await self.user_repo.update(user)
        return user

    async def delete(self, user_id: int) -> None:
        await self.user_repo.delete(user_id)

    async def get_range_report_by_tg_id(
        self, tg_id: int, start_date: date, end_date: date
    ) -> RangeReport:
        pass

