from flask_restful import Resource
from models.store_model import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message", "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Item with this name {} already exists.".format(name)}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occured while creating the store."}
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {"message": "Store deleted"}, 200


class StoreList(Resource):
    def get(self):
        return {"stores": list(map(lambda store: store.json(), StoreModel.query.all()))}
