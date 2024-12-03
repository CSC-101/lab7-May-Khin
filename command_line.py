import sys
import convert
#sum the valid float values from the command-line arguments
#input: a list of command-line arguments
#output: the sum of all valid float values
def main():
    total_sum = 0.0
    for i in sys.argv[1:]:
        converted_number = convert.str_to_float(i)
        if converted_number is not None:
            total_sum += converted_number
    print("The sum of the numbers is:", total_sum)

if __name__ == "__main__":
    print(sys.argv)
    main()
