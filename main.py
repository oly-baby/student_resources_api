from fastapi import FastAPI 
from uuid import UUID 

app = FastAPI()

students = {} 

student_resources = {
    "id":0,
    "name": "",
    "age": 0,
    "sex": "",
    "height": 0, 
}

@app.get("/")
def home():
    return{" my home psge"} 

@app.get("/students")
def get_students():
    return{"message": "this my student", "data": students}


@app.get("/students/{id}")
def get_single_student(id):
    student = students[id]
    return{"message": "succeessful", "data": students}

@app.post("/students")
def create_student(name: str, age: int, sex: str, height: float=''):
    new_student = student_resources.copy()
    id_ = len(students) + 1 
    uuid_id = str(UUID(int=id_))
    new_student['id'] = uuid_id 
    new_student['name'] = name 
    new_student['age'] = age
    new_student['sex'] = sex 
    new_student['height'] = height 


    # save the new book in the database{dictionary} 
    # new_book[uuid_id] = new_book 
    students[new_student["id"]] = new_student
    return{"messages": "successfull created", 'data': new_student}

@app.put("/students/{id}")  # PUT method to update a resource
def update_student(id: str, name: str, age: int, sex: str, height: float=''):  # A combination of path and query parameters
    student = students.get(id)
    if not student:
        return {"error": "student not found"}

    student["name"] = name
    student["age"] = age
    student["sex"] = sex
    student["height"] = height

    return {"message": "student updated successfully", "data": student}


@app.delete("/students/{id}")  # DELETE method to delete a resource
def delete_student(id: str):
    student = students.get(id)
    if not student:
        return {"error": "student not found"}

    del students[id]

    return {"message": "student deleted successfully"}


