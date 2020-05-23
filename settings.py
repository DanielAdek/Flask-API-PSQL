import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def database_string():
  return os.environ.get("DATABASE_URL")

def secret():
  return os.environ.get("SECRET")

def environment():
  return os.environ.get("APP_ENVIRONMENT")

def test_db_connection_url():
  return os.environ.get("TEST_DATABASE_URL")