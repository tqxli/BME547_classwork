# db_server.py

"""
Database format

[{
    "name": <string>,
    "id": <integer>,
    "blood_type: <string>,
    "test_name": [<string1>, <string2>, ...],
    "test_result": [<string1>, <string2>, ...]
}]

[{
    "name": <string>,
    "id": <integer>,
    "blood_type: <string>,
    "tests": {"test_name": result1, ...},
}]

"""

db = []


from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


def add_patient(patient_name, patient_id, blood_type):
    new_patient = {
        "name": patient_name,
        "id": patient_id,
        "blood_type": blood_type,
        "test_name": [],
        "test_results": []
    }
    db.append(new_patient)


def init_server():
    add_patient("A Ables", 1, "A+")
    add_patient("B Boyles", 2, "B+")
    # initialize logging


@app.route("/new_patient", methods=["POST"])
def add_new_patient_to_server():
    """
    Receive data from POST request
    Call other functions to do the work
    Return information
    """
    in_data = request.get_json()
    message, status_code = add_new_patient_worker(in_data)
    return message, status_code


def add_new_patient_worker(in_data):
    result = validate_new_patient_info(in_data)
    if result is not True:
        return result, 400

    add_patient(in_data["name"], in_data["id"], in_data["blood_type"])
    return "Patient successfully added", 200


def validate_new_patient_info(in_data):
    if type(in_data) is not dict:
        return "POST data was hont a dictionary"
    
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, datatype in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from POST data".format(key)
        if type(in_data[key]) is not datatype:
            return "Key {}'s value has wrong data type".format(key)

    return True


@app.route("/add_test", methods=["POST"])
def add_test():
    in_data = request.get_json()
    return


@app.route("/get_results/<patient_id>", methods=["GET"])
def information(patient_id):
    return


if __name__ == "__main__":
    init_server()
    app.run()