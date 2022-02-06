from flask import Flask, jsonify
from flask_restful import Resource, Api
import db
app = Flask(__name__)


def get_db():
    return db.Database()

@app.route('/')
def index():
    return "hai"

class Person(Resource):
    def get(self, name):
        self.db = get_db()
        person = self.db.getPerson(name)
        dictionary = self.db.makeDictionaries(person)
        dictionary['_id'] = str(dictionary['_id'])
        return dictionary

api = Api(app)

api.add_resource(Person, '/person/<string:name>')

app.run(debug=True)
    
    
        
    
    