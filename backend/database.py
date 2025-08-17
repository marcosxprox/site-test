import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Monta a URL de conexão
DATABASE_URL = os.environ.get("DATABASE_URL")

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Cria a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()
