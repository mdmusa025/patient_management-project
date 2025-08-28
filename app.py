from fastapi import FastAPI,path
import json

app=FastAPI()

def load_data():
    with open('pateint.json','r') as f:
        data=json.load(f)
    return data



@app.get("/")
def hello():
    return{'message':'pateint management API'}

@app.get("/about")
def about():
    return{'message':'A fully function API to manage your pateint rec '}

@app.get("/view")
def view():
    data=load_data

    return data

@app.get('/pateint{pateint_id}')
def view_pateint(pateint_id: str =path(..., description='ID of the pateint in the DB' ,example='P001')):
    # load the all pateint
    data=load_data()
 
    if pateint_id in data:
        return data[pateint_id]
    raise HTTPException(status_code=404,deatail='pateint not found')

@app.get('/sort')
def sort_pateint(sort_by:str=query(...,description='sort on the basis of height,weight or bmi'), order:str=query('asc', description='sort in asc or desc order')):
    valid_fields=['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail='invalid field select from{valid_fields}')
    
    if
         
    