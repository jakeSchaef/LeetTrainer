from algos import Algos
from helpers import get_integer_array

class menu_calls:

    def two_sum_call(self):

        two_sum_array = []

        print("You selected Two Sum!\n")

        array_iterator = int(
            input("Enter amount of integers:\n")
        )

        for i in range(array_iterator):

            try:
                value = int(
                    input("Enter value: ")
                )

                two_sum_array.append(value)

            except ValueError:
                print("Invalid data type")

        try:
            target = int(
                input("Enter target value:\n")
            )

        except ValueError:
            print("Invalid target entered")
            return None

        algos = Algos()

        pairs = algos.two_sum(
            two_sum_array,
            target
        )

        if pairs:

            print(f"\nIndex Pairs: {pairs}")

            print(
                f"Value Pairs: "
                f"{[(two_sum_array[i], two_sum_array[j]) for i, j in pairs]}"
            )

        else:
            print("No valid combos found!")

        return pairs


    def binary_search_call(self):

        print("\nQueue Binary Search\n")

        user_input = get_integer_array()

        user_input.sort()

        print(
            f"\nSorted Array: "
            f"{user_input}"
        )

        try:
            target = int(
                input(
                    "Enter target value: "
                )
            )

        except ValueError:
            print("Invalid target")
            return None

        algos = Algos()

        result = algos.binary_search(
            user_input,
            target
        )

        if result != -1:

            print(
                f"Target found at index {result}"
            )

        else:
            print("Target not found")

        return result


    def valid_parenth_call(self):

        print("\nValid Parentheses Selected\n")

        parenth_string = input(
            "Enter brackets: "
        )

        algos = Algos()

        result = algos.valid_parenth(
            parenth_string
        )

        if result:
            print("Valid Parentheses")

        else:
            print("Invalid Parentheses")

        return result
   
    def sliding_window_call(self):
       
        print("\nSliding Window Selected\n")
       
        algos = Algos()
       
        # Grab user input and provide example
        print("\nProvide a string with repeating substrings\n")
        sliding_wind_str = input("Example --> 'abcabcbb' || Input Here: ")
        # Clean the string to prevent algo failure
        clean_string = sliding_wind_str.replace(" ", "").lower()
        # Store results then return a clean output
        result = algos.sliding_window(clean_string)
       
        if result:
            print("\nHere are the results for your string...\n")
            print(f"\nUser String: {sliding_wind_str}, Longest Substring Found: Length {result}\n")
        else:
            print("No Substring Found")
           
        return result
   
    def top_k_call(self):
        k = 0
       
        print("\nSliding Window Selected\n")
       
        algos = Algos()
       
        user_input = get_integer_array()
           
        k = int(input("Input the frequency you would like to search: "))
       
        result = algos.top_k_frequency(
            user_input,
            k
            )
       
        print(f"TOP K RESULTS! --> {result}")
               
        return result
   
    def contains_dupes_call(self):
        algos = Algos()
       
        user_input = get_integer_array()
       
        result = algos.contains_dupes(user_input)
               
        return result

    def buy_stonks_call(self):
        algos = Algos()
        
        user_input = get_integer_array()

        result = algos.buy_stonks(user_input)

        print("=" * 30)
        print("\tBUY / SELL STOCKS")
        print("=" * 30)
        print(f"Prices Entered: {user_input}")
        print(f"Maximum Profit: {result}")

        return result