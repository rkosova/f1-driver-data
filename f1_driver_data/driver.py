from flask import (
    Blueprint, jsonify, request
)

from f1_driver_data.data_read import read_all


bp = Blueprint('driver', __name__, url_prefix='/driver')

@bp.route('/all', methods=['GET'])
def driver_all():
    drivers_all = read_all()
    dict_drivers = [o.get_dict() for o in drivers_all]
    return jsonify(dict_drivers)