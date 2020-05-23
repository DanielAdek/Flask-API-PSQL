from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local imports
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
  # import bucklist model
  from app.models import Bucketlist

  app = FlaskAPI(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)

  # CREATE OR RETREIVE BUCKETLIST
  @app.route('/bucketlists/', methods=["GET", "POST"])
  def bucketLists():
    if request.method == 'POST':
      # create bucketlist
      name = str(request.data.get('name', ''))
      
      if name:
        bucketlist = Bucketlist(name=name)
        bucketlist.save()
        response = jsonify({
          'id': bucketlist.id,
          'name': bucketlist.name,
          'date_created': bucketlist.date_created,
          'date_modified': bucketlist.date_modified
        })
        response.status_code = 201
        return response
    else:
      # get bucketlists
      bucketlists = Bucketlist.get_all();
      results = []

      for bucketlist in bucketlists:
          obj = {
              'id': bucketlist.id,
              'name': bucketlist.name,
              'date_created': bucketlist.date_created,
              'date_modified': bucketlist.date_modified
          }
          results.append(obj)
      response = jsonify(results)
      response.status_code = 200
      return response

  # EDIT, DELETE, OR GET ONE FROM BUCKETLIST
  @app.route('/bucketlists/<int:id>', methods=['GET', 'PUT', 'DELETE'])
  def bucketlist_manipulation(id, **kwargs):
    # retrieve a buckelist using it's ID
    bucketlist = Bucketlist.query.filter_by(id=id).first()
    if not bucketlist:
      # Raise an HTTPException with a 404 not found status code
      abort(404)

      if request.method == 'DELETE':
        bucketlist.delete()
        return {
          "message": "bucketlist {} deleted successfully".format(bucketlist.id) 
        }, 200

      elif request.method == 'PUT':
        name = str(request.data.get('name', ''))
        bucketlist.name = name
        bucketlist.save()
        response = jsonify({
          'id': bucketlist.id,
          'name': bucketlist.name,
          'date_created': bucketlist.date_created,
          'date_modified': bucketlist.date_modified
        })
        response.status_code = 200
        return response

      else:
        # GET
        response = jsonify({
          'id': bucketlist.id,
          'name': bucketlist.name,
          'date_created': bucketlist.date_created,
          'date_modified': bucketlist.date_modified
        })
        response.status_code = 200
        return response

  return app