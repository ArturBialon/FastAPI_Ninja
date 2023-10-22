
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mssql+pyodbc://kolo1:haslo@I4790K/test?driver=ODBC+Driver+17+for+SQL+Server')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
