from flask import (
    Blueprint, jsonify, request
)

from f1_driver_data.data_read import read_all


bp = Blueprint('driver', __name__, url_prefix='/driver')

@bp.route('/all', methods=['GET'])
def driver_all():
    drivers_all = read_all()
    dict_drivers = [driver.get_dict() for driver in drivers_all]
    
    if not request.args.get('category') and not request.args.get('ranking') and not request.args.get('n', type=int):
        return jsonify(dict_drivers)

    # filter category
    if request.args.get('category') and request.args.get('ranking') and request.args.get('n', type=int):
        category = request.args.get('category')
        ranking = request.args.get('ranking')
        n = request.args.get('n', type=int)

        # check if category exists
        if category not in dict_drivers[0]:
            return jsonify({'error': f'Category "{category}" does not exist'}), 400

        # Sort by given category and rank by bottom or top
        if ranking == 'bottom':
            dict_drivers.sort(key=lambda x: x[category])
        elif ranking == 'top':
            dict_drivers.sort(key=lambda x: x[category], reverse=True)
        else:
            return jsonify({'error': 'Invalid value for "ranking". It should be "top" or "bottom"'}), 400

        # take n drivers
        dict_drivers = dict_drivers[:n]

    else:
        return jsonify({'error': 'Both "n",  "category" and "ranking" are required query parameters'}), 400

    return jsonify(dict_drivers)


@bp.route('/<driver_name>', methods=['GET'])
def driver_by_name(driver_name):
    drivers_all = read_all()
    matching_drivers = [o.get_dict() for o in drivers_all if o.name == driver_name]
    
    if not matching_drivers:
        return jsonify({'error': 'Driver not found'}), 404

    return jsonify(matching_drivers[0])