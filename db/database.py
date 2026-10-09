import sqlite3

from tools.questions import QUESTIONS
DATABASE = 'open.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn 