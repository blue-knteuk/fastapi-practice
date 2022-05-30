from sqlalchemy import (Column, BigInteger, String, DateTime, Enum, ForeignKey)
import enum
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class GenderType(str, enum.Enum):
    male = "男"
    female = "女"
    other = "その他"

class JobType(str, enum.Enum):
    engineer = "エンジニア"
    designer = "デザイナー"
    projectmanager = "プロジェクトマネージャー"
    producer = "プロデューサー"
    qa = "QA"
    sales = "セールス"
    marketer = "マーケター"

class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, nullable=False, primary_key=True, autoincrement=True)
    belongs = relationship("Belongs", back_populates="user")
    name = Column(String(255), nullable=False, default=1)
    birth = Column(DateTime, nullable=False)
    gender = Column(Enum(GenderType, values_callable=lambda x: [e.value for e in x]), nullable=True)
    mail = Column(String(255), nullable=False)
    job = Column(Enum(JobType, values_callable=lambda x: [e.value for e in x]), default=None)
    work_at = Column(DateTime, default=None)
    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=False, server_default=current_timestamp())

class Divisions(Base):
    __tablename__ = 'divisions'
    id = Column(BigInteger, nullable=False,  primary_key=True, autoincrement=True)
    belongs = relationship("Belongs", back_populates="division")
    name = Column(String(255), nullable=False, default=1)
    leader_user_id = Column(BigInteger, nullable=False)
    start_at = Column(DateTime, nullable=False)

class Belongs(Base):
    __tablename__ = 'belongs'
    id = Column(BigInteger, nullable=False,  primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="SET NULL"), nullable=False, default=1)
    division_id = Column(BigInteger, ForeignKey("divisions.id", ondelete="SET NULL"), nullable=False)
    start_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    end_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    user = relationship("Users", back_populates="belongs")
    division = relationship("Divisions", back_populates="belongs")
