from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Async engine
async_engine = create_async_engine(DATABASE_URL, echo=False, future=True)

# Async session factory
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

# Declarative base
Base = declarative_base()

