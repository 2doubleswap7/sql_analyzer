import asyncpg

from asyncpg.connection import Connection
from asyncpg.cursor import Cursor
from typing import Dict, Any

async def get_db_connection(db_config: Dict[str, Any]):
    conn: Connection = asyncpg.connect(
        host=db_config["host"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"]
    )
    return conn

async def execute_explain_analyze(conn: Connection, query: str) -> str:
    with conn.cursor() as cursor:
        cursor.execute(f"EXPLAIN ANALYZE {query}")
        result = cursor.fetchall()
    return "\n".join(row[0] for row in result)
