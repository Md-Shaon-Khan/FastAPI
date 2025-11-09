from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    weight: float
    married: bool
    allergies:List[str]
    contact_details: Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self
    
    
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
    
patient_info = {
    "name": "Shaon",
    "email": "shaon@hdfc.com",
    "age": 73,
    "weight": 65.5,
    "married": False,
    "allergies": ["Dust", "Pollen"],
    "contact_details": {
        "phone": "01567903274",
        "address": "Dhaka",
        "emergency": "01712345678"
    }
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)