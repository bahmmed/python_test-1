def formatting_advance_string(data):
    # Print the table header
    print("{:<15} {:<5}".format("Name", "Age"))
    print("-" * 20)

    # Print each row of the table
    for emp in data:
        print("{:<15} {:<5}".format(emp["name"], emp["age"]))

# Example data: a list of dictionaries with names and ages
emp_data = [
    {"name": "Mr. Mamun", "age": 25},
    {"name": "Mr. Abu taher", "age": 30},
    {"name": "Mr. Abu Saleh", "age": 22},
    {"name": "Mr. Tuhin", "age": 28},
]

# Display the information in a formatted table
formatting_advance_string(emp_data)
