def input_weight_entry():
    print("Enter patient weight in form of ## units (e.g., 105 lb)")
    weight_input = input("Enter weight: ")
    weight_in_kg = parse_weight_input(weight_input)
    print("The patient weight of {} kg will be stored "
          "in database.".format(weight_in_kg))


def parse_weight_input(weight_input):
    num_of_spaces = weight_input.count(" ")
    if num_of_spaces != 1:
        return None
    weight, units = weight_input.split(' ')
    try:
        weight = float(weight) # be able to take both int and float inputs
    except:
        return
    units = units.lower() # for unified unit names
    if units in ["lb", "pound"]:
        weight_kg = convert_lb_to_kg(weight)
    elif units in ["kg"]:
        weight_kg = weight
    weight_kg = round(weight_kg)
    return weight_kg


def convert_lb_to_kg(weight_lb):
    weight_kg = weight_lb / 2.20462
    return weight_kg


if __name__ == "__main__":
    input_weight_entry()
