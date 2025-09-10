from typing import Callable, Optional
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


a_engine = create_async_engine("sqlite+aiosqlite:///database.db")
a_sessionmaker = async_sessionmaker(a_engine, expire_on_commit=False)


async def a_get_db():
    async with a_sessionmaker() as db:
        yield db


def a_connection(isolation_level: Optional[str] = None):
    """
    Декоратор для управления асинхронными транзакциями с настраиваемым уровнем изоляции.

    Args:
        isolation_level: Уровень изоляции транзакции:\n
        "READ COMMITTED"\n
        "REPEATABLE READ"\n
        "SERIALIZABLE"\n
        Если None, используется
        уровень по умолчанию базы данных.
    """

    def decorator(method: Callable):
        async def wrapper(*args, **kwargs):
            async with a_sessionmaker() as session:
                try:
                    if isolation_level:
                        await session.execute(
                            text(f"BEGIN TRANSACTION ISOLATION LEVEL {isolation_level}")
                        )

                    result = await method(*args, **kwargs, session=session)
                    await session.commit()
                    return result

                except Exception as e:
                    await session.rollback()
                    raise e
                finally:
                    await session.close()

        return wrapper

    return decorator
