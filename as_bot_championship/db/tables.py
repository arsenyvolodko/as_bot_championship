from sqlalchemy import BigInteger, Column, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import DateTime
from datetime import datetime

from as_bot_championship.enums.answer_status_enum import AnswerStatusEnum


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=False,
    )

    username: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )


class Hall(Base):
    __tablename__ = "hall"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    hall_id: Mapped[int] = mapped_column(ForeignKey("hall.id"), nullable=False)


class Service(Base):
    __tablename__ = "service"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    chat_id = Column(BigInteger, nullable=False)


class Option(Base):
    __tablename__ = "option"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    comment: Mapped[str] = mapped_column(nullable=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("service.id"), nullable=False)


class Request(Base):
    __tablename__ = "request"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    user_id = Column(
        BigInteger,
        ForeignKey("user.id"),
        nullable=False,
    )

    text: Mapped[str] = mapped_column(nullable=True)

    service_id: Mapped[int] = mapped_column(nullable=False)
    location_id: Mapped[int] = mapped_column(nullable=False)
    option_id: Mapped[int] = mapped_column(nullable=False)

    status: Mapped[AnswerStatusEnum] = mapped_column(
        nullable=False, default=AnswerStatusEnum.IGNORED
    )

    time = Column(DateTime, nullable=False, default=datetime.now)

    source_chat_msg_text: Mapped[str] = mapped_column(nullable=True)
    common_chat_msg_text: Mapped[str] = mapped_column(nullable=True)

    source_chat_msg_id = Column(
        BigInteger,
        nullable=True,
    )

    common_chat_msg_id = Column(
        BigInteger,
        nullable=True,
    )
