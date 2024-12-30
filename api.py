from flask import Flask , jsonify , request

app = Flask(__name__)



items = [
    {"id": 1 , "name":"Item1" , "Description":"This is 1st item"},
    {"id": 2 , "name":"Item2" , "Description":"This is 2nd item"},
    {"id": 3 , "name":"Item3" , "Description":"This is 3rd item"}
]

@app.route("/")
def home():
    return "Welcome to TO Do List"


## retrieve all items

@app.route("/items",methods=['Get'])
def get_items():
    return jsonify(items)


## retrieve a specific item by id

@app.route('/items/<int:items_id>',methods=['Get'])
def get_byID(items_id):
    item = next((item for item in items if item["id"]==items_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)


## Post create a new item 

@app.route("/items",methods=['Post'])
def create():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    
    new_item = {
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json["name"],
        "Description":request.json["Description"]

    }
    items.append(new_item)
    return jsonify(new_item)


##put:update item

@app.route('/items/<int:items_id>',methods=['Put'])
def update(items_id):
    item = next((item for item in items if item["id"]==items_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['name']= request.json.get('name',item['name'])
    item['Description']= request.json.get('Description',item['Description'])
    return jsonify(item)


## Delete item
@app.route('/items/<int:item_id>', methods=['Delete'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "item deleted"})






if __name__=="__main__":
    app.run(debug=True)