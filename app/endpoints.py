from flask import Flask, jsonify, abort, make_response, request, url_for

from app import app
from app import task_model
from app import task_service as ts

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = ts.get_tasks()
    return jsonify({'tasks': tasks})

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = ts.get_task(task_id)
    return jsonify({'task': task})

@app.route('/task', methods=['POST'])
def add_task():
    new_task = ts.add_task(request.json)
    return jsonify({'task': new_task}), 201

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):

    task = ts.update_task(task_id, request.json)

    return jsonify({'task': task})

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = ts.delete_task(task_id)
    return jsonify({'result': task})
