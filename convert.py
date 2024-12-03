#convert a string to a float, or return None if conversion fails
#input: string
#output:  float or None
#use try and except to handle the conversion and return the result
def str_to_float(value: str) -> float:
    try:
        return float(value) #convert the string to a float
    except ValueError:
        return None #return None if the conversion fails
