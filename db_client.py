import requests


out_data = {"name": "charlie", "id": 3, "blood_type": "AB"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=out_data)
print(r.status_code)
print(r.text)

out_data = {"id": 3, "test_name": "hdl", "test_result": 400}
r = requests.post("http://127.0.0.1:5000/add_test", json=out_data)
print(r.status_code)
print(r.text)

r = requests.get("http://127.0.0.1:5000/get_results/3")
print(r.status_code)
print(r.json())

# r = requests.get("http://127.0.0.1:5000/")
# print(r.text)