from typing import Generator

##############################################
# BLOCK FOR COMMON INTERACTION WITH DATABASE #
##############################################
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

import settings

# create async engine for interaction with database
engine = create_async_engine(settings.REAL_DATABASE_URL,
                             future=True,
                             echo=True,
                             execution_options={"isolation_level": "AUTOCOMMIT"}
                             )

# create session for interaction with database
async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
