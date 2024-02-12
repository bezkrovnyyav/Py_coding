"""
In user.json file we have information about users in format 
[{“id”: 1, “name”: “userName”, “department_id”: 1}, ...], 

in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...]. 

Function user_with_department(csv_file, user_json, department_json) 
should read from json files information and create csv file in format:

header line - name, department

next lines :  <userName>, <departmentName>

If file department.json doesn't contain department with department_id 
from user.json we generate DepartmentName exception.

Create appropriate json-schemas for user and department.

If schema for user or department doesn't satisfy formats described above 
we should generate InvalidInstanceError exception  

To validate instances create function validate_json(data, schema)
"""
import json
import jsonschema
from jsonschema import validate
import csv


class DepartmentName(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InvalidInstanceError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def validate_json(json_data, validation_schema):
    try:
        validate(instance=json_data, schema=validation_schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


student_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"},
        },
        "required": ["department_id", "name"]
    }
}

department_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
    }
}


def user_with_department(user_csv, user_json, department_json):
    with open(user_json, "r") as f:
        users = json.load(f)
        if not validate_json(users, student_schema):
            raise InvalidInstanceError("Error in user schema")
    with open (department_json, "r") as f:
        departments = json.load(f)
        if not validate_json(departments, department_schema):
            raise InvalidInstanceError("Error in department schema")
    
    id_name_dict = dict((element["id"], element["name"]) for element in departments)

    user_with_dep = []
    for elem in users:
        try:
            user_with_dep.append({"name": elem["name"], "department": id_name_dict[elem["department_id"]]})
        except Exception:
            raise DepartmentName("Department with id {} doesn't exists".format(elem["department_id"]))

    with open(user_csv, "wt") as f:
        csv.writer = csv.DictWriter(f, fieldnames=["name", "department"])
        csv.writer.writeheader()
        csv.writer.writerows(user_with_dep)


user_with_department("my.csv", "json_for_test/user.json", "json_for_test/department_without_id.json")
