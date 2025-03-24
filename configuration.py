import os
class Config:
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://concesionario:concesionario@DESKTOP-M9L8G75/concesionario?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False