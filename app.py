from robyn import Robyn, jsonify
import models
from database import Base, engine, session_local
from sqlalchemy.orm import Session
from handlers import create_items, all_items
from sqlalchemy import select
import json
import uuid
from models import Items
from rodi import Container


Base.metadata.create_all(engine)

def get_session():
    session = session_local()
    try:
        yield session
    finally:
        session.close()

app = Robyn(__file__)

container = Container()
session_instance = container.add_instance(get_session())
session = Session(session_instance)



@app.get("/")
async def h(request):
    return "Hello, world!"

@app.get("/items")
async def items(request, session = session):
    print("here")
    print(request)
    
    items =  session.query(models.Items).all()
    print(items)
    print("here 2x")
    return {"status_code":200, "body": "all", "type": "json"} 

@app.get("/item")
async def items(request, session = session):
    print("here")
    print(request)
    
    items =  session.query(models.Items).get('c81103a1-6d42-4129-a39e-006dea46b191')
    print(items)
    print("here 2x")
    return {"status_code":200, "body": "all", "type": "json"} 

@app.post("/item")
async def new_item(request, session = session):
    body = bytearray(request['body']).decode("utf-8")
    json_body = json.loads(body)
    name = json_body['name']
    print(name)
    
    item_id = uuid.uuid4()
    new_item = Items(id=item_id, name=name)
    print(new_item.__dict__)

    session.add(new_item)
    
    return {"status_code":201, "body": jsonify(new_item.__dict__['name']), "type": "json"}


app.start(port=8000, url="0.0.0.0")