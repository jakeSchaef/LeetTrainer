from datetime import datetime

"""
Functions Dedicated to Touching Files
"""        
def save_results(
        user_name,
        algorithm,
        result):

    with open(
            "results.txt",
            "a") as file:

        timestamp = datetime.now()

        file.write(
            f"Date: {timestamp} | "
            f"User: {user_name} | "
            f"Algo: {algorithm} | "
            f"Result: {result}\n"
        )

def read_results():
    file = open("results.txt", "r")
    print("=" * 40)
    print("\t\tHISTORY")
    print("=" * 40)
    for line in file:
        print(line.strip())
           
    file.close()

def return_latest():
    file = open("results.txt", "r")
    latest_entry = file.readlines()
    print("=" * 30)
    print("\tLATEST ENTRY...")
    print("=" * 30)
    if latest_entry:
        print(latest_entry[-1].strip())
    else:
        print("No history found.")