from flask import (
    Blueprint, jsonify, request
)


bp = Blueprint('driver', __name__, url_prefix='/driver')

@bp.route('/all', methods=['GET'])
def driver_all():
    