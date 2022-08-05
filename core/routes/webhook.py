import sys
from flask import jsonify, request
from flask_classful import FlaskView, route
from core.services.publisher import Publisher


class Webhook(FlaskView):

    def __init__(self):
        self.pub = Publisher()


    @route('/create/data_product', methods=['POST'])
    @route('/create/data_product/', methods=['POST'])
    def create_product(self):
        try:
            body = request.json

            if 'type' not in body or not body['type']:
                return jsonify({
                    'code':  'BAD_REQUEST',
                    'message': 'type is required'}), 400

            if 'name' not in body or not body['name']:
                return jsonify({
                    'code':  'BAD_REQUEST',
                    'message': 'name is required'}), 400

            if 'owner' not in body or not body['owner']:
                return jsonify({
                    'code':  'BAD_REQUEST',
                    'message': 'owner is required'}), 400

            response = self.pub.producer(key='create_data_product', value=body)
            return jsonify(response), 200

        except Exception as e:
            error = f'{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}'
            print(error, file=sys.stderr, flush=True)
            return jsonify({
                'code':  'INTERNAL_SERVER_ERROR',
                'message': 'An unhandled error was ocurred'}), 500
