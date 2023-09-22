from flask import Flask, jsonify, url_for

def create_app():
    app = Flask(__name__, instance_relative_config=True)


    @app.route("/hello")
    def hello():
        return 'Hello, World!'
    
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
    
    return app