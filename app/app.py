from flask import Flask

def create_app():
    """Create a Hello world app

    Returns:
        [return] -- [Flask app]
    """
    app = Flask(__name__)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def index():
        return 'Hello World!'
    return app
