import os


HOST = os.getenv("HOST", "localhost")
PORT = os.getenv("PORT", 27017)
DB_NAME = os.getenv("DB_NAME", "scrapegoat")
USERNAME = os.getenv("USERNAME", "scrapegoat")
PASSWORD = os.getenv("PASSWORD", "scrapegoat")
DEFAULT_COLLECTION = os.getenv("DEFAULT_COLLECTION", "extracted_data")

