from django.apps import AppConfig
import psycopg2  # Import the PostgreSQL driver

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        try:
            from django.db import connections
            connection = connections['default']
            connection.ensure_connection()
            if connection.is_usable():
                print("\n.....Connected to PostgreSQL successfully! \n")
        except Exception as e:
            print(f"Database connection failed: {e}")
