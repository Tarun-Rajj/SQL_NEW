from flask import Flask



# Route for Add Task
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity,User
from models.models import db, Task, User, Role

admin = Blueprint('admin', __name__)

@admin.route('/tasks', methods=['GET'])
@jwt_required()
def view_all_tasks():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user).first()

    if user.role.name == 'ADMIN':
        tasks = Task.query.all()
        task_list = []
        for task in tasks:
            task_list.append({
                'id': task.id,
                'title': task.title,
                'status': task.status,
                'assigned_to': task.assigned_to_user.username,
                'assigned_by': task.assigned_by_user.username
            })
        return jsonify(tasks=task_list), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 403