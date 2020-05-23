import os

from app import create_app
from settings import environment

config_name = environment() # config_name = "development"
app = create_app(config_name)

@app.route("/")
def slash():
  return "Welcome to bucketlist api"

if __name__ == '__main__':
  app.run()