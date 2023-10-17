from flask import Flask, jsonify, url_for
from flask_apispec import FlaskApiSpec

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    docs = FlaskApiSpec(app)

    @app.route("/hello")
    def hello():
        return 'Hello, World!'
    docs.register(hello)
    
    from . import driverBp
    app.register_blueprint(driverBp.bp)

    @app.route("/health")
    def health():
        status = 'OK'
        all = driverBp.driver_all().status_code
        dname = driverBp.driver_by_name('Lewis Hamilton')[1]
        if all != 200 or dname != 200:
            status = "Damaged"


        return jsonify({"status" : status, "all": all, "driver_name": dname}), 200
    docs.register(health())
    


    return app