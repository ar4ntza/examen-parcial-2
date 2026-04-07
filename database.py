# base de datos :)
import mysql.connector
from motor.motor_asyncio import AsyncIOMotorClient

# ── MySQL ─────────────────────────────────────────────────────────────────────
def get_mysql_conn():
    conn = mysql.connector.connect(
        host= "localhost",
        port= 3306,
        user= "root",
        password= "timo",           
        database= "ecommerce_db"
    )
    return conn

# ── MongoDB ───────────────────────────────────────────────────────────────────
MONGO_DETAILS = "mongodb+srv://ar4ntzagarcia_db_user:timito@admindb.uspvdrq.mongodb.net/?appName=admindb"

mongo_client= AsyncIOMotorClient(MONGO_DETAILS)
mongo_db= mongo_client["ecommerce_logs"]
eventos_collection= mongo_db.get_collection("eventos_usuario")
