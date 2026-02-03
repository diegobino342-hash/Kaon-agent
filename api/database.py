import sqlite3
from datetime import datetime

class KaonMemory:
    def __init__(self):
        self.conn = sqlite3.connect('kaon_knowledge.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS insights 
            (id INTEGER PRIMARY KEY, symbol TEXT, timestamp TEXT, 
             pattern_dna TEXT, result TEXT, confidence REAL)''')
        self.conn.commit()

    def save_experience(self, symbol, dna, result, conf):
        self.cursor.execute("INSERT INTO insights (symbol, timestamp, pattern_dna, result, confidence) VALUES (?,?,?,?,?)",
                           (symbol, datetime.now().isoformat(), str(dna), result, conf))
        self.conn.commit()
