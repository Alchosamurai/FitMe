from app.database.database import a_connection
from typing import Optional
from app.models.user_model import UserBase, UserTargetBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class AsyncUserRepo:
    @a_connection()
    async def get_by_tg_id(
        self, tg_id: int, session: AsyncSession
    ) -> Optional[UserBase]:
        result = await session.execute(select(UserBase).where(UserBase.tg_id == tg_id))
        return result.scalar_one_or_none()

    @a_connection()
    async def get(self, user_id: int, session: AsyncSession) -> Optional[UserBase]:
        result = await session.execute(select(UserBase).where(UserBase.id == user_id))
        return result.scalar_one_or_none()

    @a_connection()
    async def create(self, user: UserBase, session: AsyncSession) -> UserBase:
        existing_user = await self.get_by_tg_id(user.tg_id, session)
        if existing_user:
            return existing_user
        session.add(user)
        await session.commit()
        return user

    @a_connection()
    async def update(self, user: UserBase, session: AsyncSession) -> UserBase:
        updated_user = await session.merge(user)
        await session.commit()
        return updated_user

    @a_connection()
    async def delete(self, user_id: int, session: AsyncSession) -> None:
        user = await self.get(user_id, session)
        if user:
            await session.delete(user)
            await session.commit()


class AsyncTargetRepo:
    @a_connection()
    async def get(
        self, user_daily_id: int, session: AsyncSession
    ) -> Optional[UserTargetBase]:
        query = select(UserTargetBase).where(UserTargetBase.id == user_daily_id)
        target = await session.execute(query)
        return target.scalar_one_or_none()

    @a_connection()
    async def get_by_user_tg_id(
        self, user_tg_id: int, session: AsyncSession
    ) -> Optional[UserTargetBase]:
        result = await session.execute(
            select(UserTargetBase).where(UserTargetBase.user_tg_id == user_tg_id)
        )
        return result.scalar_one_or_none()

    @a_connection()
    async def get_by_user_tg_id_or_default(
        self, user_tg_id: int, session: AsyncSession
    ) -> Optional[UserTargetBase]:
        return await self.get_by_user_tg_id(user_tg_id, session) or UserTargetBase(
            user_tg_id=user_tg_id,
            target_cal=0,
            target_protein=0,
            target_fat=0,
            target_carbohydrates=0,
        )

    @a_connection()
    async def create(
        self, user_daily: UserTargetBase, session: AsyncSession
    ) -> UserTargetBase:
        existing_user_daily = await self.get_by_user_tg_id(
            user_daily.user_tg_id, session
        )
        if existing_user_daily:
            return existing_user_daily
        session.add(user_daily)
        await session.commit()
        return user_daily

    @a_connection()
    async def update(self, user_daily: UserTargetBase, session: AsyncSession) -> None:
        await session.merge(user_daily)
        await session.commit()
        return

    @a_connection()
    async def delete(self, user_daily_id: int, session: AsyncSession) -> None:
        user_daily = await self.get(user_daily_id, session)
        if user_daily:
            await session.delete(user_daily)
            await session.commit()
