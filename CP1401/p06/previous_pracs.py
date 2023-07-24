#1
def main():
    worker_level = get_valid_level("Worker Level :" ,1 ,10)
    total_salary = get_total_salary(worker_level)
    print(f"With worker level {worker_level}, your salary is ${total_salary:,.2f}")

def get_valid_level(prompt ,low ,high):
    worker_level = int(input(prompt))
    while worker_level < low or worker_level > high:
        print("invalid worker level")
        worker_level = int(input("Worker Level :"))
    return worker_level

def get_total_salary(worker_level):
    total_salary = worker_level * 5000
    return total_salary

main()

#2
def main():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    print_grid(rows ,columns)

def print_grid(rows ,columns):
    for i in range(rows):
        for j in range(columns):
            print(j, end=" ")
        print()

main()