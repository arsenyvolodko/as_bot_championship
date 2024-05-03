from sqlalchemy import BigInteger, Column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from atomskills_org_bot.enums.service_name_enum import ServiceNameEnum


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Column = Column(
        BigInteger,
        primary_key=True,
        autoincrement=False,
        nullable=False,
        unique=True,
        index=True,
    )

    username: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )

    request_status: Mapped[ServiceNameEnum] = mapped_column(
        nullable=True,
        default=None,
    )
