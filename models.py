from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Text, Float, ForeignKey, ARRAY

from database import Base

# TODO: think more about how the relationship(), back_populates, and cascade works

class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    strava_auth_code: Mapped[Optional[str]] = mapped_column(Text)
    spotify_auth_code: Mapped[Optional[str]] = mapped_column(Text)

    activities: Mapped[List["Activity"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"


class Activity(Base):
    __tablename__ = "activity"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id", ondelete="CASCADE"))
    name: Mapped[Optional[str]] = mapped_column(Text)
    distance: Mapped[Optional[float]] = mapped_column(Float)
    moving_time: Mapped[Optional[float]] = mapped_column(Float)
    total_elevation_gain: Mapped[Optional[float]] = mapped_column(Float)
    speed_avg: Mapped[Optional[float]] = mapped_column(Float)
    speed_max: Mapped[Optional[float]] = mapped_column(Float)
    speed_var: Mapped[Optional[float]] = mapped_column(Float)
    heartrate_avg: Mapped[Optional[float]] = mapped_column(Float)
    heartrate_max: Mapped[Optional[float]] = mapped_column(Float)
    cadence_over_time: Mapped[Optional[List[int]]] = mapped_column(ARRAY(Integer))

    user: Mapped["User"] = relationship(back_populates="activities")

    def __repr__(self) -> str:
        return f"Activity(id={self.id!r}, name={self.name!r}, user_id={self.user_id!r})"
