from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from sqlalchemy import Column, Boolean, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import settings
from sqlalchemy.dialects.postgresql import UUID
import uuid
import re
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import validator

##############################################
# BLOCK FOR COMMON INTERACTION WITH DATABASE #
##############################################

# create async engine for interaction with database
engine = create_async_engine(settings.REAL_DATABASE_URL, future=True, echo=True)