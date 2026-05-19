from fastapi import FastAPI,Path,HTTPException,Query
# By using the path we can imporve the Path Readability and use for the data validation
import json
app = FastAPI();

def load_file():
    with open("patient.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"Hello": "World"}
@app.get("/patients")
def get_patients():
    data = load_file()
    return data 

@app.get("/patient/{id}")
#path params
def get_patient_id(id:str = Path(...,description="this is the id",example ="1")):
    # load all the Patients
    data = load_file()
    if id in data:
        return data[id] 
    # return "Error Message"
    raise HTTPException(status_code = 404,detail="Patient not found")

@app.get("/sort")
#query params
def sort_patient(sort_by:str = Query(...,description="Sort by age"),order:str= Query('asc',description='sort in asc or des')):
    vaild_fields=["age"];
    # error handling
    if sort_by not in vaild_fields:
        raise HTTPException(status_code=404,detail=f"Invalid Select from {vaild_fields}")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail='Invalid select from the asc and Desc')
    data = load_file();
    sort_order = True if order=="desc" else False
    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data
