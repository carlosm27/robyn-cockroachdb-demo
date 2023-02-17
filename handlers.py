from models import Items
import uuid


def all_items(session):
    items = session.query(Items).all()
    return items


def create_items(session, name):
    item_id = uuid.uuid4()
    new_item = Items(id=item_id, name=name)
    session.add(new_item)
    return new_item

def get_item(id:uuid, session):
    item = session.query(Items).get(id)
    return item

def delete_item(id:int, session):
    item = session.query(Items).get(id)
    session.delete(item)
    session.commit()
    session.close()
    return item