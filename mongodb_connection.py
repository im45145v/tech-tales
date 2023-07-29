from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data, cache_resource

import pymongo

class MongoConnect(ExperimentalBaseConnection[pymongo.MongoClient]):

    def _connect(self, **kwargs) -> pymongo.MongoClient:
        return pymongo.MongoClient(**kwargs)
    
    def database(self, db:str = None, coll:str = None, ttl: int = 3600):
        @cache_resource(ttl=ttl)
        def _database(db: str = None, coll: str = None):
            return self._instance[db]
        return _database(db, coll)
        
        
    def collection(self, db:str = None, coll:str = None, ttl: int = 3600):
        @cache_resource(ttl=ttl)
        def _collection(db: str = None, coll: str = None):
            return self._instance[db][coll]
        return _collection(db, coll)
    
    
    def client(self):
        return self._instance
    
    
    def insert_one(self, dbname: str, collname: str,*args, **kwargs):
        if 'ttl' in kwargs:
            ttl=kwargs.pop('ttl')
        else:
            ttl=3600
        @cache_data(ttl=ttl)
        def _insert_one(dbname: str, collname: str, *args, **kwargs):
            coll= self.collection(dbname,collname)
            coll.insert_one(*args, **kwargs)
        return _insert_one(dbname, collname, *args, **kwargs)
    
    def find(self, dbname: str, collname: str,*args, **kwargs):
        coll= self.collection(dbname,collname)
        items = coll.find(*args, **kwargs)
        items = list(items)
        return items

    
    def find_one(self, dbname: str, collname: str,*args, **kwargs):
        coll= self.collection(dbname,collname)
        document = coll.find_one(*args, **kwargs)
        return document
    
    
    def update_one(self, dbname: str, collname: str,*args, **kwargs):
        def _update_one(dbname: str, collname: str, *args, **kwargs):
            coll= self.collection(dbname,collname)
            coll.update_one(*args, **kwargs)
        return _update_one(dbname, collname, *args, **kwargs)