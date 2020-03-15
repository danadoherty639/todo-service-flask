import psycopg2
from app.config import config

def connect():
    """Connect to postgres server"""
    conn = None

    params = config()

    print('Connecting to postgres database')
    conn = psycopg2.connect(**params)

    return conn
