import time
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Field Signal Filter API",
    description="سيرفر سحابي آمن لتصفية الإشارات الميدانية",
    version="1.0.0"
)

DB_NAME = "field_experiments.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS experiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            raw_signal REAL,
            stability_factor REAL,
            phase_angle REAL,
            status TEXT,
            clean_value REAL,
            processing_time_ms REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()
