# Day 8 Assignment 

dog = dict()
dog = {"name": "Mujaheed", "color": "Black", "breed": "pug", "legs": 4, "age": 4}
student_dictionary = {
    "first_name": "Mujaheed",
    "last_name": "Abdullahi",
    "gender": "M",
    "age": 26,
    "marital_status": "unmarried",
    "skills": ["Data_Scientest"],
    "country": "Nigeria",
    "city": "Bauchi",
    "address": "Bauchi",
}
print(len(student_dictionary))
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))
student_dictionary["skills"].append("travelling")
list_keys = list(student_dictionary.keys())
list_values = list(student_dictionary.values())
list_of_tuples = [(k, v) for k, v in student_dictionary.items()]
student_dictionary.pop("marital_status")
del dog