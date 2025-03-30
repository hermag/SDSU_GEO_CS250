import os
import time
from datetime import datetime
from sqlalchemy import create_engine

# while True:
#     some_var = os.environ.get('SOME_VAR', 'default_value')
#     print(f"Hello, there, the environment variable is {some_var}! it's {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#     time.sleep(5)

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')

engine = create_engine(f'postgresql+psycopg2://{db_username}:{db_password}@{db_host}/{db_name}')
