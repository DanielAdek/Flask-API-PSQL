import os
from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand

# import local files
from app import db, create_app
from app import models
from settings import environment


app = create_app(config_name=environment())
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()