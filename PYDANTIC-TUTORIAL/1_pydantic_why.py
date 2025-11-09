from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name: str = Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 chars',examples=['Shaon','Raunaq'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt = 0 , lt = 120)
    weight: Annotated[float,Field(gt=0,strict=True)]
    married: Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies: Optional[List[str]] = None
    contact_details: Optional[Dict[str,str]] = None
    
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('Updated')
    
patient_info = {'name': 'Shaon','email':'shaon@gmail.com','linkedin_url':'https://www.linkedin.com/feed/', 'age':21, 'weight':62,  'allergies':['pollen','dust'], 'contact_details':{'email':'shaon@gmail.com','phone':'01567903274'}}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)