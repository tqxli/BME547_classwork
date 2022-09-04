def get_user_input(test):
    level = input("Enter your {} level: ".format(test))
    level = float(level)
    return level

def check_HDL(hdl):
    if hdl >= 60:
        return "Normal"
    elif hdl >= 40:
        return "Borderline Low"
    else:
        return "Low"

def check_LDL(ldl):
    if ldl < 130:
        return "Normal"
    elif ldl < 160:
        return "Borderline High"
    elif ldl < 190:
        return "High"
    else:
        return "Very High"

def driver(test):
    level = get_user_input(test)
    if test == "HDL":
        results = check_HDL(level)
    elif test == "LDL":
        results = check_LDL(level)
    output_results(test, level, results)

def output_results(test, level, results):
    print("Your {} level is {}. This is {}.".format(test, level, results))

def interface():
    print("My Program")
    print("Options:")
    print("1 - Run HDL Analysis")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    while choice != '9':        
        if choice == '1':
            driver()
        print("Options:")
        print("1 - Run HDL Analysis")
        print("9 - Quit")
        choice = input("Enter your choice: ")

    return
   
interface()