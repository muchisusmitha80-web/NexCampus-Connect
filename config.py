import os
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'nexcampus_diet_academic_platform_2026_key')
    
    # Database configuration
    DB_TYPE = os.environ.get('DB_TYPE', 'sqlite').lower()
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_PORT = os.environ.get('MYSQL_PORT', '3306')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'nexcampus_diet')

    # Construct DB URI
    if DB_TYPE == 'mysql':
        # URL encode password if necessary or plain
        if MYSQL_PASSWORD:
            SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8mb4"
        else:
            SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8mb4"
    else:
        # SQLite default for zero-friction local development / testing
        base_dir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(base_dir, 'nexcampus.db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 280,
        'pool_pre_ping': True,
    } if DB_TYPE == 'mysql' else {}

    # DIET Institutional Branding Constants
    COLLEGE_NAME = "Dhanekula Institute of Engineering & Technology"
    COLLEGE_SHORT_NAME = "DIET"
    PLATFORM_NAME = "NexCampus"
    CAMPUS_ADDRESS = "Ganguru, Vijayawada, Krishna District, Andhra Pradesh - 521139"
    CAMPUS_EMAIL = "diet.principal@diet.ac.in"
    CAMPUS_PHONE = "+91 866 2583842"
    CAMPUS_WEBSITE = "https://diet.ac.in"
