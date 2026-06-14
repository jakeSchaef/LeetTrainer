from file_utils import (
    save_results,
    read_results,
    return_latest
)

from analytics import view_statistics

def menu():

    menu_call = menu_calls()

    user_name = input(
        "Welcome to LeetTrainer!\n"
        "Enter your full name:\n"
    )

    print("=" * 40)

    print(
        f"\nHi {user_name}, "
        f"welcome to LeetTrainer!"
    )

    while True:

        print("\nSelect Algorithm:\n")

        print(
            "1. Two Sum\n"
            "2. Binary Search\n"
            "3. Valid Parentheses\n"
            "4. Test Sliding Window\n"
            "5. Top K Frequent Element\n"
            "6. Contains Duplicates\n"
            "7. Buy/Sell Stocks\n"
            "8. Read Back Results\n"
            "9. Return Latest Log\n"
            "10. Run Analytics\n"
            "E. Exit"
        )

        user_selection = (
            input(
                "\nEnter selection: "
            )
            .strip()
            .upper()
        )

        if user_selection == "1":

            result = (
                menu_call
                .two_sum_call()
            )

            save_results(
                user_name,
                "Two Sum",
                result
            )

        elif user_selection == "2":

            result = (
                menu_call
                .binary_search_call()
            )

            save_results(
                user_name,
                "Binary Search",
                result
            )

        elif user_selection == "3":

            result = (
                menu_call
                .valid_parenth_call()
            )

            save_results(
                user_name,
                "Valid Parentheses",
                result
            )
           
        elif user_selection == "4":
            result = (
                menu_call
                .sliding_window_call()
                )
           
            save_results(
                user_name,
                "Longest Substring",
                result
                )
           
        elif user_selection == "5":
            result = (
                menu_call
                .top_k_call()
                )
           
            save_results(
                user_name,
                "Top K Element",
                result
                )
           
        elif user_selection == "6":
            result = (
                menu_call  
                .contains_dupes_call()
                )
           
            if result:
                formatted = " | ".join(f"Value: {n}, Count: {c}" for n, c in result.items())
            else:
                formatted = "No duplicates"
           
            save_results(
                user_name,
                "Contains Duplicates",
                formatted
                )

        elif user_selection == "7":
            result = (
                menu_call  
                .buy_stonks_call()
                )
            
            save_results(
                user_name,
                "Buy Stocks",
                result
                )

        elif user_selection == "8":
            read_results()

        elif user_selection == "9":
            return_latest()
           
        elif user_selection == "10":
            view_statistics()

        elif user_selection == "E":

            print("\nGoodbye!")

            break

        else:

            print(
                "\nInvalid Option\n"
            )

if __name__ == "__main__":
    menu()