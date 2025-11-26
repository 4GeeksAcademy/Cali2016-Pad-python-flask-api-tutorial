from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body) 
    return jsonify(todos)    

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
        return jsonify(todos)
    else:
        return jsonify({"error": "Todo not found"}), 404
    
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if 0 <= todo_id < len(todos):
        request_body = request.get_json(force=True)
        todos[todo_id] = request_body
        return jsonify(todos)
    else:
        return jsonify({"error": "Todo not found"}), 404