from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Gurgaon', 'state': 'Haryana', 'pin': '122001'}
address1 = Address(**address_dict)

patient_dict = {'name': 'Nitish', 'gender': 'Male', 'age': 35, 'address': address1}
patient1 = Patient(**patient_dict)

full_dump = patient1.model_dump()
print("Full dump:", full_dump)

partial_dump = patient1.model_dump(include={'name', 'address'})
print("\nPartial dump (name + address):", partial_dump)

nested_partial_dump = patient1.model_dump(include={'address': {'city', 'pin'}})
print("\nNested dump (only city and pin):", nested_partial_dump)

print("\nType of dump:", type(partial_dump))
