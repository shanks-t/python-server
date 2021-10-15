import sqlite3
import json
from models import Employee, Location


EMPLOYEES = [
    {
        "id": 1,
        "name": "Jessica Younker",
        "email": "jessica@younker.com"
    },
    {
        "id": 2,
        "name": "Jordan Nelson",
        "email": "jordan@nelson.com"
    },
    {
        "id": 3,
        "name": "Zoe LeBlanc",
        "email": "zoe@leblanc.com"
    },
    {
        "name": "Meg Ducharme",
        "email": "meg@ducharme.com",
        "id": 4
    },
    {
        "name": "Hannah Hall",
        "email": "hannah@hall.com",
        "id": 5
    },
    {
        "name": "Emily Lemmon",
        "email": "emily@lemmon.com",
        "id": 6
    },
    {
        "name": "Jordan Castelloe",
        "email": "jordan@castelloe.com",
        "id": 7
    },
    {
        "name": "Leah Gwin",
        "email": "leah@gwin.com",
        "id": 8
    },
    {
        "name": "Caitlin Stein",
        "email": "caitlin@stein.com",
        "id": 9
    },
    {
        "name": "Greg Korte",
        "email": "greg@korte.com",
        "id": 10
    },
    {
        "name": "Charisse Lambert",
        "email": "charisse@lambert.com",
        "id": 11
    },
    {
        "name": "Madi Peper",
        "email": "madi@peper.com",
        "id": 12
    },
    {
        "name": "Jenna Solis",
        "email": "jenna@solis.com",
        "id": 14
    },
    {
        "name": "Eric \"Macho Man\" Taylor",
        "email": "macho@man.com",
        "id": 22
    },
    {
        "name": "trey shanks",
        "email": "trey@shanks.com",
        "id": 23
    }
]


def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute('''
            SELECT
              a.id,
              a.name,
              a.address,
              a.location_id,
                l.name location_name,
                l.address location_address
            FROM Employee a
            JOIN Location l
                ON l.id = a.location_id
    ''')

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            employee = Employee(row['id'], row['name'], row['address'],row['location_id'])

            location = Location(row['id'], row['location_name'], row['location_address'])

        # Add the dictionary representation of the location to the animal
            employee.location = location.__dict__

        # Add the dictionary representation of the employee to the list
            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)


# Function with a single parameter
def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
        FROM employee a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'])

        return json.dumps(employee.__dict__)


def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the employeeS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def find_employees_by_location(location_id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT *
        FROM employee a
        WHERE a.location_id = ?
        """, (location_id, ))
        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['breed'],
                                row['status'], row['location_id'], row['customer_id'])
            employees.append(employee.__dict__)
    return json.dumps(employees)
