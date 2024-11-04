from flask import Flask, jsonify, request

app = Flask(__name__)

# Фіктивні дані для прикладу
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

# GET (отримання даних)
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# POST (створення нового ресурсу)
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify(new_item), 201

# PUT (оновлення існуючого ресурсу)
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = next((item for item in data if item["id"] == id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    item.update(request.get_json())
    return jsonify(item)

# DELETE (видалення ресурсу)
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = next((item for item in data if item["id"] == id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    data.remove(item)
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
