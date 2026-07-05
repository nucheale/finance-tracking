from sqlalchemy import ForeignKey, Text, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone
from connection import engine


class Base(DeclarativeBase):
    pass


class User(Base):
    """Таблица пользователей"""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(Text(), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(timezone.utc))


class Shop(Base):
    """Справочник наименований магазинов"""

    __tablename__ = "shops"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    origin_name: Mapped[str] = mapped_column(Text(), unique=True, nullable=False)
    readable_name: Mapped[str] = mapped_column(Text())
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))


class Category(Base):
    """Справочник категорий расходов и доходов"""

    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text(), unique=True, nullable=False)
    type: Mapped[str] = mapped_column(Text())  # доход / расход


class Account(Base):
    """Таблица банковских счетов (карт)"""

    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(Text(), nullable=False)
    bank_name: Mapped[str] = mapped_column(Text(), nullable=False)
    currency: Mapped[str] = mapped_column(Text(), nullable=False)


class Transaction(Base):
    """Таблица транзакций (операций по счетам)"""

    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id", ondelete="CASCADE"))
    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id", ondelete="CASCADE"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))
    amount: Mapped[float] = mapped_column(Float(), nullable=False)
    date_time: Mapped[datetime] = mapped_column(nullable=False)


def create_tables() -> None:
    Base.metadata.create_all(engine)
