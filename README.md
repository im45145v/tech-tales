# Streamlit MongoDB Connection

Connect to [MongoDB](https://mongodb.com/) and MongoDB Atlas from your [Streamlit](https://streamlit.io/) app.

## Quick demonstration

```python
import streamlit as st
from tech-tales import mongodb_connection.py

client= st.experimental_connection('mongo',type=MongoConnect, host=st.secrets['mclient'])
db = "Tech_Tales"
collection = "comments"
user_data = client.find_one(db, collection, {"username": username})
comments = user_data.get("comments", [])
for each_comment in comments:
    st.write(each_comment)
```



## Main methods

### collection()

```python
client.collection(self, db:str = None, coll:str = None, ttl: int = 3600)

```
Returns and caches a MongoDB collection object with the parameters specified

#### update_one()

```python
client.update_one(dbname: str, collname: str,*args, **kwargs) -> None

Example:
client.update_one(db, collection,
        {"username": username},
        {"$addToSet": {"comments": comment}}
    )
```

Executes a MongoDB command to update a single document



#### find_one()

```python
client.find_one(dbname: str, collname: str,*args, **kwargs)

Example:
user_document = client.find_one(db, collection, {"username": username})

```

Executes a MongoDB query to find a single document

#### insert_one()

```python
insert_one(self, dbname: str, collname: str,*args, **kwargs)

Example: 
user_data = {
        "username": username,
        "comments": [comment],
        "number": []
    }
    client.insert_one(db, collection, user_data)
```
This will insert one new value into the database


## Configuration

The connection configuration can be:

- passed via connection kwargs
- passed through environmental variables
- stored in Streamlit's [secrets.toml](https://docs.streamlit.io/library/advanced-features/secrets-management) file (~/.streamlit/secrets.toml on Linux)

You can find more information about managing connections in [this section](https://docs.streamlit.io/library/advanced-features/connecting-to-data#global-secrets-managing-multiple-apps-and-multiple-data-stores) of Streamlit documentation 

Most important parameters:

- `mclient` - MongoDB URI (Atlas URI or mongodb://localhost:27017)

## Usage examples



##### Test_app.py

```python
import streamlit as st
from mongodb_connection import MongoConnect
client= st.experimental_connection('testdb', type=MongoConnect, host=st.secrets['mclient'])
db = "Tech_Tales"
collection = "comments"
user_data = client.find_one(db, collection, {"username": 'im45145v'})
if user_data:st.write("Exists")
else:st.write("Not Exists")
```
This program check if a particular username exists within the database



##### 1_💬_Confess.py.py (inside pages)
This file allows you to add a comment for a particular user



## Configuration Examples



##### connection kwargs

```python
client= st.experimental_connection('testdb', type=MongoConnect, host="mongodb+srv://<uname>:<pass>@cluster0.xxxyyyz.mongodb.net/?retryWrites=true&w=majority")

```

##### secrets.toml

```toml
account_sid = ''
auth_token = ''
twilio_phone_number = ''
mclient = "mongodb+srv://<uname>:<pass>@cluster0.xxxyyyz.mongodb.net/?retryWrites=true&w=majority"
```
account_sid,auth_token,twilio_phone_number are twilio based things in this demo app
