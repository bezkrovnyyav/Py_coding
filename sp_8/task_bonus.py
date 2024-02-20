"""
1. Create users and subjects data from files

get_subjects_from_json(subjects_json) -> List[Subject]

get_users_with_grades(users_json, subjects_json, grades_json) -> List[User]

2. Simulate working with the application

method User.create_user(username, password, role) creates user

method user.add_score_for_subject(subject:Subject, score: Score) adds score for subject

function add_user(user, users) adds user to users (in case of uniqueness username)

function add_subject(subject, subjects) adds subject to subjects (in case of uniqueness title)

function get_grades_for_user(username:str, user:User, users:list) 
returns all grades for the user with username (only own grades or for mentor)

3. Rewrite the old json-files with new ones

users_to_json(users, json_file)

subjects_to_json(subjects, json_file)

grades_to_json(users, subjects, json_file)
"""

import json

def get_users_with_grades(users_json,subjects_json,grades_json):
    with open(users_json) as u_file, open(subjects_json) as s_file, open(grades_json) as g_file:
        users = json.load(u_file)
        subjects = json.load(s_file)
        grades = json.load(g_file)
        print(users)
        print(subjects)
        print(grades)

        # [{'username': 'Trainee1', 'id': '31abd085e3474ec68fdd182ec9709b0a', 'role': 0,       'password': '$2b$12$sYWHQzY0ch2hzDSMccAs.uIaliO/SA3sky/GKMH5o70Z/rMtyWh1W'}]
        # [{'title': 'Mathematics', 'id': '31abd085e3474ec68fdd182ec9709d0a'},      {'id': '31abd085e3474ec68fdd182ed9709b0a', 'title': 'Software Design'}]
        # [{'user_id': '31abd085e3474ec68fdd182ec9709b0a', 'subject_id': '31abd085e3474ec68fdd182ed9709b0a',       'score': 'B'},      {'user_id': '31abd085e3474ec68fdd182ec9709b0a', 'subject_id': '31abd085e3474ec68fdd182ec9709d0a',           'score': 'C'}]

    return users