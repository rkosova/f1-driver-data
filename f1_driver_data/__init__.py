from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)


    @app.route("/hello")
    def hello():
        return 'Hello, World!'
    
    from . import driverBp
    app.register_blueprint(driverBp.bp)
    
    return app