import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="ep-cool-fire-ait9uqpz-pooler.c-4.us-east-1.aws.neon.tech",
        port="5432",
        user="neondb_owner",
        password="npg_PKXTMQyWp82i",
        dbname="neondb",
        sslmode="require"
    )