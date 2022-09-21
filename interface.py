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


def check_total_cholesterol(total_cholesterol):
    if total_cholesterol < 200:
        return "Normal"
    elif total_cholesterol < 240:
        return "Borderline High"
    else:
        return "High"


def driver(test):
    if test == "HDL":
        level = get_user_input(test)
        results = check_HDL(level)
    elif test == "LDL":
        level = get_user_input(test)
        results = check_LDL(level)
    elif test == "Total Cholesterol":
        hdl = get_user_input("HDL")
        results = check_HDL(hdl)
        output_results("HDL", hdl, results)
        ldl = get_user_input("LDL")
        results = check_LDL(ldl)
        output_results("LDL", ldl, results)
        level = hdl + ldl
        results = check_total_cholesterol(level)
    output_results(test, level, results)


def output_results(test, level, results):
    print("Your {} level is {}. This is {}.".format(test, level, results))


def interface():
    print("My Program")
    keep_running = True
    while keep_running:     
        print("Options:")
        print("1 - Run HDL Analysis")
        print("2 - Run LDL Analysis")
        print("3 - Run Total Cholesterol Analysis")
        print("9 - Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            driver("HDL")
        elif choice == '2':
            driver("LDL")
        elif choice == '3':
            driver("Total Cholesterol")
        elif choice == '9':
            keep_running = False

    return
   
# interface()