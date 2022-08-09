import os
import urllib3
import settings
from flask import Flask
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
urllib3.disable_warnings()
started_date = datetime.now()

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS', settings.BaseConfig)
    app.config.from_object(app_settings)
    CORS(app)

    # routes
    from core.routes.health import Health
    Health.register(app, route_base='/')

    from core.routes.webhook import Webhook
    Webhook.register(app, route_base='/webhook')

    return app
