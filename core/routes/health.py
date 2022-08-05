import sys
import tomli
from flask import jsonify
from datetime import datetime
from core.app import started_date
from flask_classful import FlaskView, route


class Health(FlaskView):

    @route('/', methods=['GET'])
    def health_check(self):
        try:
            with open('pyproject.toml', mode='rb') as tm:
                config = tomli.load(tm)
                cfg = config['tool']['poetry']

                response = {
                    'status': 'Healthy',
                    'name': cfg['name'],
                    'version': cfg['version'],
                    'started': started_date.strftime('%b %d %Y %H:%M:%S'),
                    'uptime': str(datetime.now() - started_date)
                }
                return jsonify(response), 200

        except Exception as e:
            error = f'{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}'
            print(error, file=sys.stderr, flush=True)
            return jsonify({
                'code':  'INTERNAL_SERVER_ERROR',
                'message': 'An unhandled error was ocurred'}), 500
