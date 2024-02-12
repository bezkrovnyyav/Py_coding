"""Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
This class should contain method serialize for serialize object to filename according to  type. 
For defining format create enum FileType with values JSON, BYTE.
Create function serialize(object, filename, fileType).
This function should serialize object to filename according to type.
For example:
if user_dict = { 'name': 'Roman', 'id': 8}
then
serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String
"""
import json
import pickle
from enum import Enum


class SerializeManager:

    def __init__(self, filename, fileType):
        self.filename = filename
        self.fileType = fileType.value

    def __enter__(self):
        if self.fileType == 1:
            self.file = open(self.filename, "w")
        if self.fileType == 2:
            self.file = open(self.filename, "wb")
        return self
    
    def __exit__(self, type, value, traceback):
        self.file.close()

    def serialize(self, obj):
        if self.fileType == 1:
            json.dump(obj, self.file)
        if self.fileType == 2:
            pickle.dump(obj, self.file)
    

class FileType(Enum):
    JSON = 1
    BYTE = 2


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


user_dict = {'name': 'Roman', 'id': 8}
serialize(user_dict, "2.txt", FileType.BYTE)
serialize("String", "string.json", FileType.JSON)