"""
Class Student has attributes full_name:str, avg_rank: float, courses: list
Class Group has attributes title: str, students: list.

Make both classes JSON serializable. 

Json-files represent information about student (students). 

Create methods:  

Student.from_json(json_file) that return Student instance from attributes from json-file;

Student.serialize_to_json(filename)

Group.serialize_to_json(list_of_groups, filename)

Group.create_group_from_file(students_file)

Parse given files, create instances of Student class and create instances of Group class 
(title for group is name of json-file without extension).
"""
import json
from json import JSONEncoder


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, json_file):
        with open(json_file, "r") as file:
            data = json.load(file)
            return cls(**data)
       
    def serialize_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self.__dict__, json_file)

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"
    
    def to_dict(self):
        return {"full_name": self.full_name, "avg_rank": self.avg_rank, "courses": self.courses}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["full_name"], data["avg_rank"], data["courses"])

class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __str__(self):
        student_str = [f"{student.full_name} ({student.avg_rank}): {student.courses}" for student in self.students]
        return f"{self.title}: {student_str}"

    def to_dict(self):
        return {"title": self.title, "students": [student.to_dict() for student in self.students]}
    
    def serialize_to_json(self, filename):
        with open(filename, 'w') as json_file:
            json.dump(self, json_file, cls=MyEncoder)

    @classmethod
    def create_group_from_file(cls, students_file):
        result = []
        with open(students_file) as file:
            data = json.load(file)
            if type(data) is dict:
                result.append(Student.from_dict(data))
            elif type(data) is list:
                for person in data:
                    result.append(Student.from_dict(person))
        title = students_file.split('.')[0]
        return cls(title, result)

class MyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Student, Group)):
            return obj.to_dict()
        return super(MyEncoder, self).default(obj)


std1 = Student("Victor", 5.5, ["C++", "Python"])
user1 = Student.from_json("test.json")
print(user1)