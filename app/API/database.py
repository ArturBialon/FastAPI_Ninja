
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# I4790K = nazwa serwera
# kolo1 = login
# haslo = hasło
engine = create_engine('mssql+pyodbc://kolo1:haslo@I4790K/test?driver=ODBC+Driver+17+for+SQL+Server') #that should be stored somwhere safe, like system ENV Variables
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
