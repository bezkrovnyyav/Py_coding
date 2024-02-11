"""
Create function find(file, key)
This function parses json-file and returns all unique values of the key.

1.json:
[{"name": "user_1”, "password": "pass_1”},
{"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
find("1.json", "password") returns ["pass_1", "qwerty"]

2.json:
[{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, 
{"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]

3.json:
{"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
find("3.json", "password") returns ["1234qweQWE"
"""
import json

def find(file, key):
    with open(file, 'r') as temp:
        data = json.load(temp)
            
    def get_value(obj, key):
        if type(obj) is list:
            result_data = []
            for item in obj:
                result_data.extend(get_value(item, key))
            return result_data
        elif type(obj) is dict:
            result_data = []
            if key in obj:
                if type(obj[key]) is str:
                    result_data.append(obj[key])
                else: 
                    result_data.extend(obj[key])
            for item in obj.values():
                if type(item) is dict or type(item) is list:
                    result_data.extend(get_value(item, key))
            return result_data
        else: return []
    
    data = list(set((get_value(data, key))))
    return data


print(find("1.json", "password"))
print(find("2.json", "password"))