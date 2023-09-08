from flask import (
    Blueprint, jsonify, request
)

from f1_driver_data.data_read import read_all


bp = Blueprint('driver', __name__, url_prefix='/driver')

@bp.route('/all', methods=['GET'])
def driver_all():
    if request.args.get('driver_name'):
        res = driver_by_name(request.args.get('driver_name'))
        return res
    elif request.args.get('ranking') == 'bottom':
        n = request.args.get('n', type=int)
        category = request.args.get('category')
        res = bottom_n_drivers_by_category(number=n, category=category)
        return res


    drivers_all = read_all()
    dict_drivers = [o.get_dict() for o in drivers_all]
    return jsonify(dict_drivers)


def driver_by_name(driver_name):
    print(driver_name)
    drivers_all = read_all()
    matching_drivers = [o.get_dict() for o in drivers_all if o.name == driver_name]
    
    if not matching_drivers:
        return jsonify({'error': 'Driver not found'}), 404

    return jsonify(matching_drivers[0])


def bottom_n_drivers_by_category(category, number):
    # get query parameters
    if number is None or category is None:
        return jsonify({'error': 'Both "number" and "category" are required query parameters'}), 400
    
    # sort drivers by give category
    drivers_all = read_all()
    sorted_drivers = sorted(drivers_all, key=lambda driver: getattr(driver, category))

    # Take the bottom 'n' drivers
    bottom_n_drivers = [driver.get_dict() for driver in sorted_drivers[:number]]

    return jsonify(bottom_n_drivers)