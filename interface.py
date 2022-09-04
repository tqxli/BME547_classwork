from cgitb import handler


def get_user_input():
    level = input("Enter: ")
    return level

def check_HDL(hdl):
    if hdl >= 60:
        return "Normal"
    elif hdl >= 40:
        return "Borderline Low"
    else:
        return "Low"

def driver():
    hdl_level = get_user_input()
    results = check_HDL(hdl_level)
    output_results(hdl_level, results)

def output_results(hdl_level, results):
    print("Your HDL level is {}. This is {}".format(hdl_level, results))

def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    while choice != '9':
        choice = input("Enter your choice: ")
    return
   
interface()