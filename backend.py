#!/usr/bin/python
from typing import Dict
import psycopg2
from configparser import ConfigParser

class connection:    

    def __init__(self) -> None:
        self.dbconnection = self.connect()

    def closeconnection(self) -> None:
        self.dbconnection.close()

    
    def config(self, filename='databaseinfo.ini', section='postgresql') -> Dict:
        
        parser = ConfigParser()
        
        parser.read(filename)

        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db


    def connect(self) -> psycopg2._connect:
        conn = None
        try:
            
            params = self.config()

            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
    
            cur = conn.cursor()
        
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)
            
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                print('Database connection established.')
                return conn 

    def executequery(self) -> str:
        pass

con = connection()

con.dbconnection.close()
print('Database connection closed.')