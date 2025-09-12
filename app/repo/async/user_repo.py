from app.database.database import a_connection
from typing import Optional
from app.models.user_model import UserBase
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
    async def get_by_tg_id():
        pass
