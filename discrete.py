# discretes = non-iterables

def print_names():
    print(person_1_name)
    print(person_2_name)
    print(person_3_name)

def prompt_for_person_number():
    prompt = "What number person's name would you like to see? "
    answer = input(prompt)
    person_number = int(answer)
    return person_number

def print_person_name(number):
    if number == 1:
        print(person_1_name)
    elif number == 2:
        print(person_2_name)
    elif number == 3:
        print(person_3_name)
    else:
        raise UnknownPerson


def update_person_name(number, new_name):
    if number == 1:
        person_1_name = new_name
    elif number == 2:
        person_2_name = new_name
    elif number == 3:
        person_3_name = new_name
    else:
        raise UnknownPerson

print("Haris" < "Nia")  # Prints True

print("Samir" < "Evander")  # Prints False


def print_two_names_in_order():
    if person_1_name < person_2_name:
        print(person_1_name)
        print(person_2_name)
    else:
        print(person_2_name)
        print(person_1_name)
