from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

import pymongo

class MongoConnect(ExperimentalBaseConnection[pymongo.MongoClient]):

    def _connect(self, **kwargs) -> pymongo.MongoClient:
        return pymongo.MongoClient(**kwargs)
    
    def database(self, db:str, **kwargs):
            return self._instance.get_database(db, **kwargs)
        
        
    def collection(self, db:str = None, coll:str = None):
        return self._instance.get_database(db).get_collection(coll)
    
    
    def client(self):
        return self._instance
    
    def find(self, dbname: str, collname: str,*args, **kwargs):
        if 'ttl' in kwargs:
            ttl=kwargs.pop('ttl')
        else:
            ttl=3600
        @cache_data(ttl=ttl)
        def _find(dbname: str, collname: str, *args, **kwargs):
            coll= self.collection(dbname,collname)
            items = coll.find(*args, **kwargs)
            items = list(items)
            return items
        return _find(dbname, collname, *args, **kwargs)
    
    def find_one(self, dbname: str, collname: str,*args, **kwargs):
        if 'ttl' in kwargs:
            ttl=kwargs.pop('ttl')
        else:
            ttl=3600
        @cache_data(ttl=ttl)
        def _find_one(dbname: str, collname: str, *args, **kwargs):
            coll= self.collection(dbname,collname)
            document = coll.find_one(*args, **kwargs)
            return document
        return _find_one(dbname, collname, *args, **kwargs)
    
    
    def insert_one(self, dbname: str, collname: str,*args, **kwargs):
        if 'ttl' in kwargs:
            ttl=kwargs.pop('ttl')
        else:
            ttl=3600
        @cache_data(ttl=ttl)
        def _insert_one(dbname: str, collname: str, *args, **kwargs):
            coll= self.collection(dbname,collname)
            document = coll.insert_one(*args, **kwargs)
            return document
        return _insert_one(dbname, collname, *args, **kwargs)
    
    def update_one(self, dbname: str, collname: str,*args, **kwargs):
        if 'ttl' in kwargs:
            ttl=kwargs.pop('ttl')
        else:
            ttl=3600
        @cache_data(ttl=ttl)
        def _update_one(dbname: str, collname: str, *args, **kwargs):
            coll= self.collection(dbname,collname)
            document = coll.update_one(*args, **kwargs)
            return document
        return _update_one(dbname, collname, *args, **kwargs)