import convert
# ask the user to enter numbers and returns a list of valid floats
#input: string or "done"
def gather_numbers() -> list[float]:
    num = []
    while True:
        user_input = input("Enter a number or 'done' to end the program:\n ").strip()
        if user_input.lower() == "done":
            break
        converted_number = convert.str_to_float(user_input) #convert the input to a float
        if converted_number is not None:
            num.append(converted_number) #add to the list
    return num



if __name__ == "__main__":
    num = gather_numbers()
    print("The list of the numbers :", num)

