import os

class SecretConfig:
    def get_postgres_config(self):
        return {
            "host": os.getenv("POSTGRES_HOST"),
            "database": os.getenv("POSTGRES_DB"),
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD"),
            "port": int(os.getenv("POSTGRES_PORT", 5432)),
            "sslmode": os.getenv("POSTGRES_SSLMODE", "require")
        }