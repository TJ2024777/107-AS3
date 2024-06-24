from flask import Flask, request
import json

items = []
app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "hello from the test page"



# API endpoints
# JSON
# create an API to perform a get resquest to this url: /api/about
# return your name as a message 



# create an API to perform a get resquest to this url: /api/about

@app.get("/api/about")
def about():
    me ={"name" :"Terry J"}
    return json.dumps(me)

@app.post("/api/product")
def saveProducts():
    product = request.get_json()
    print(product)
    #mock the save
    items.append(product)
    return json.dumps(product)

@app.get("/api/products")
def getProduct():
    return json.dumps(items)    


# create an API to perform a get resquest to this url: /api/about


app.run(debug = True)