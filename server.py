import os
from core.app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host=os.getenv('HOST', ''), port=os.getenv('PORT', ''))
