from flask import Blueprint
from controllers.user_controller import index, show, create, edit, destroy

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/create', methods=['POST'])(create)
# user_bp.route('/<int:user_id>', methods=['GET'])(show)
# user_bp.route('/edit/<int:user_id>', methods=['PUT'])(edit)
# user_bp.route('/delete/<int:user_id>', methods=['DELETE'])(destroy)