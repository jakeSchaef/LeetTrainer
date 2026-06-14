"""
Helper Function for Array Values
"""    
def get_integer_array():
    numbers = []
   
    stop_binary_input = "Y"
   
    print("\nProvide an array of numbers. If you wish to continue/stop input using 'Y/N'\n")
   
    while stop_binary_input == "Y" or stop_binary_input == "y":
        try:
            array_value = int(input("Provide a number for the array: "))
            numbers.append(array_value)
           
        except ValueError:
            print("Invalid Data Type...")
           
        stop_binary_input= input("Continue? (Y/N): ")
       
    return numbers