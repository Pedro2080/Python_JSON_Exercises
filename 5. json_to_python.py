import json

python_dict =  '{"name": "Joao Pedro", "age": 18}'
python_list =  '["Red", "Green", "Black"]'
python_str =  '"Python Json"'
python_int =  '1234'
python_float =  '21.34'

json_obj = json.loads(python_dict)
json_list = json.loads(python_list)
json_str = json.loads(python_str)
json_num1 = json.loads(python_int)
json_num2 = json.loads(python_float)

print("json obj : ", json_obj)
print("jason list : ", json_list)
print("json string : ", json_str)
print("json number1 : ", json_num1)
print("json number2 : ", json_num2)
