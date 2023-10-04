# Create an empty dictionary to store employee details
employee_details = {}
   
# Function to add an employee
def add_employee():
    domain = input("Enter the domain: ")
    name = input("Enter the name: ")
    empid = input("Enter the employee ID: ")
    email = input("Enter the email: ")
    
    # Store the employee details in a dictionary
    employee = {
        'Domain': domain,
        'Name': name,
        'Employee ID': empid,
        'Email': email
    }
    
    # Add the employee to the dictionary of employee details
    employee_details[empid] = employee

# Function to print employee details
def print_employee_details(empid):
    employee = employee_details.get(empid)
    if employee:
        print("\nEmployee Details:")
        for key, value in employee.items():
            print(f"{key}: {value}")
    else:
        print("\nEmployee not found.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add Employee")
    print("2. Print Employee Details")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        empid = input("Enter the employee ID to print details: ")
        print_employee_details(empid)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select a valid option.")
