import requests

# Making a GET request to GitHub to get list of branches in a repository
URL = "http://vcm-7631.vm.duke.edu:5002"
r = requests.get(URL+"/get_patients/tl299")
if r.status_code == 200:
    patient = r.json()
    ID1 = patient["Recipient"]
    ID2 = patient["Donor"]
    print("Recipient: {}, Donor: {}".format(ID1, ID2))
else:
    print("Bad request: {}".format(r.text))

blood_type1 = requests.get(URL+"/get_blood_type/{}".format(ID1))
print(blood_type1.text)
blood_type2 = requests.get(URL+"/get_blood_type/{}".format(ID2))
print(blood_type2.text)


answer = {"Name": "tl299", "Match": "No"}
# # Making a POST request to the name server
r = requests.post(URL+"/match_check",
                  json=answer)
print(r)
print(r.text)

# # Making a GET request to the name server
# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)

# # POSTing and GETing to/from the message server
# msg = {"user": "daw74", "message": "hello daw"}
# r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message",
#                   json=msg)

# r1 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/daw74")
# print(r1.text)