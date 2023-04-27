from pydantic import BaseModel, EmailStr, constr


class SignupData(BaseModel):
    name: constr(max_length=20)
    last_name: constr(max_length=20)
    email: EmailStr
