from fastapi import FastAPI,path
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
import json

app=FastAPI()

class pateint(BaseModel):

    id=Annotated[str,Field(..., description='ID of the pateint',example=['poo1'])]
    name:Annotated[str,Field(...,description='name of the pateint')]
    city:Annotated[str,Field(...,description='city where the pateint is living')]
    age:Annotated[int,Field(...,gt=0,lt=120,description='age of the pateint')]
    gender:Annotated[Literal['male','female','other'],Field(...,description='gender of the pateint')]
    height:Annotated[float,Field(...,gt=0,description='height of pateint in mtrs')]
    weight:Annotated[float,Field(...,gt=0,description="weight of patient in kgs")]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return 'underweight'
        elif self.bmi<25:
            return 'normal'
        elif self.bmi<30:
            return'overweight'
        else:
            return 'obese'
class patientupdate(BaseModel):

    id=Annotated[optional[str],Field(default=None)]
    name:Annotated[optional[str],Field(default=None)]
    city:Annotated[optional[str],Field(default=None)]
    age:Annotated[optional[int],Field(default=None,gt=0)]
    gender:Annotated[optional[Literal['male','female','other']],Field(default=None)]
    height:Annotated[optional[float],Field(default=None,gt=0)]
    weight:Annotated[optional[float],Field(default=None,gt=0)]



def load_data():
    with open('pateint.json','r') as f:
        data=json.load(f)
    return data

def save_data():
    with open('pateint.json','w') as f:
        json.dump(data,f)
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
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='invalid order select between asc and desc')
    data=load_data()

    sort_order=True if order=='desc' else False

    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0), reverse=sort_order)

    return sorted_data

@app.post('/create')
def create_pateint(pateint:pateint):
    data=load_data()
    if pateint.id in data:
        raise HTTPException(status_code=400,detail='pateint already exists')
    data[pateint.id]=pateint.model_dump(exclude=['id'])

    save_data(data)
    return JSONResponse(status_code=201,content={'message':'pateint created successfully'})

@app.put('/edit{pateint_id}')
def update_patient(pateint_id: str,patient_update:patientupdate):
     
     data=load_data()

     if pateint_id in data: 
         raise HTTPException(status_code=404,detail='pateint not found')
     existing_pateint_info=data[pateint_id]

     update_pateint_info=patient_update.model_dump(exclude_unset=True)

     for key,value in update_pateint_info.items():
         existing_pateint_info[key]=value
    
    # existing_paateint-info ->pydantic object ->updated bmi+verdict
     existing_patient_info['id']=pateint_id
     pateint_pydantic_obj=pateint(**existing_pateint_info)

    #  pydantic_obejct->dict
     existing_patient_info = pateint_pydantic_obj.model_dump(exclude='id')

     data[pateint_id]=existing_pateint_info

     save_data(data)
     return JSONResponse(status_code=200,content={'message':'pateint updated'})

@app.delete('/delete/{pateint_id}')
def delete_pateint(pateint_id:str):
    data=load_data()

    if pateint_id not in data:
        raise HTTPException(status_code=404,detail='pateint not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200,content={'message'='pateint deleted '})
    
         
    