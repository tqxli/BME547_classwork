def create_patient_entry(first_name, last_name, patient_id, patient_age):
    new_patient = {
        "First name": first_name,
        "Last name": last_name,
        "Id": patient_id,
        "Age": patient_age,
        "Tests": []
    }

    return new_patient

def get_full_name(patient):
    full_name = "{}_{}",format(patient["First name", patient["Last name"]])
    return full_name

def print_database(database):
    for patient in database:
        print("Name: {}, id: {}, Age: {}".format(
            get_full_name(patient), 
            patient["Id"],
            patient["Age"],
            )
        )

#def find_patient(db, patient_id):
#    return db[patient_id]

def add_test_to_patient(db, id_no, test_name, test_value):
    if id_no in db.keys():
        db[id_no]["Tests"].append([test_name, test_value])
    
    return db

def minor_or_adult(patient):
    if patient["Age"] >= 18:
        return "adult"
    return "minor"