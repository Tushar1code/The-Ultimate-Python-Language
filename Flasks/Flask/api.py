from flask import Flask, jsonify , request

app = Flask(__name__)

items = [
    {"id" : 1, "name": "item 1" , "description": "this is item 1"},
    {"id": 2, "name": "item 2","description": "this is item 1"}
]
@app.route('/')
def home():
    return "welcome to the sample To-do list app"

##Get: Retrieve all the items

@app.route('/items',methods = ['GET'])
def get_items():
    return jsonify(items)

## Get retrieve specific item by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items["id"]==item_id),None)
    if item is None:
        return jsonify({"error": "item not found"})
    return jsonify(item)

##Post: create a new task
@app.route('/items',methods=['post'])
def create_item():
    if not request.json or not 'name' in request.json:
        return  jsonify({"error": "item not found"})
    new_item={
        "id": items[-1]["id"]+1 if items else 1,
        "name": request.json['name'],
        "description":request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)

if __name__ == '__main__':
    app.run(debug=True)