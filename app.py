from flask import Flask
from flask_restful import Resource, Api, reqparse
import random

app = Flask(__name__)
api = Api(app)


class Query(Resource):
    """Class for query endpoint"""

    def __init__(self):
        """create argument parser"""
        self.args_parser = reqparse.RequestParser()
        # raw string of query
        self.args_parser.add_argument('query')

    def get(self):
        """Method to handle query request from the front end"""
        # parse the URL params
        args = self.args_parser.parse_args()
        query = args['query']

        # function to get resulting doc_ids (placeholder)
        doc_ids = [int(random.random() * 1000) for i in range(10)]
        return {'query': query,
                'results': doc_ids}


class Stats(Resource):
    """Class for the stats endpoint"""

    def __init__(self):
        """create argument parser"""
        super().__init__()
        self.args_parser = reqparse.RequestParser()
        # stats to be passed back
        self.args_parser.add_argument('stats')

    def post(self):
        """take in """
        args = self.args_parser.parse_args()
        stats = args['stats']

        # add results to database
        print(stats)
        # return status
        return {'status': 'ok'}


api.add_resource(Query, '/query')
api.add_resource(Stats, '/stats')

if __name__ == '__main__':
    app.run(debug=True)
