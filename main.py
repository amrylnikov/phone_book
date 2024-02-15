from collections import namedtuple

Record = namedtuple('Record', ['last_name', 'first_name', 'surname', 'organization', 'work_phone', 'personal_phone'])

def load_data(file_path: str) -> list[Record]:
    """
    Loads data from text file and return list of records.
    
    Parameters:
    - file_path (str): Path to the file.

    Returns:
    - list[Record]: List of records in namedtuple format.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        records = [Record(*line.strip().split(',')) for line in lines]
    return records

def save_data(file_path: str, records: list[Record]) -> None:
    """
    Saves records in text file.

    Parameters:
    - file_path (str): Path to the file for data saving.
    - records (list[Record]): List of records in namedtuple format.
    """
    with open(file_path, 'w') as file:
        for record in records:
            file.write(','.join(record) + '\n')

def display_records(records: list[Record], page_size: int = 10) -> None:
    """
    Display records by pages.

    Parameters:
    - records (list[Record]): List of records in namedtuple format.
    - page_size (int): Number of records on one page.
    """
    for i in range(0, len(records), page_size):
        page = records[i:i + page_size]
        for counter, record in enumerate(page):
            print(f'{i + counter}: {record}')
        input("Press Enter to continue...")

def add_record(records):
    """
    Add new record into phone book.

    Parameters:
    - records (list[Record]): List of records in namedtuple format.
    """
    last_name: str = input("Enter last name: ")
    first_name: str = input("Enter first name: ")
    surname: str = input("Enter middle name: ")
    organization: str = input("Enter organization: ")
    work_phone: str = input("Enter work phone: ")
    personal_phone: str = input("Enter personal phone: ")
    
    new_record = Record(last_name, first_name, surname, organization, work_phone, personal_phone)
    records.append(new_record)
    print("Запись успешно добавлена!")

def edit_record(records):
    """
    Edit existing record in phone book
    Редактирует существующую запись в справочнике.

    Параметры:
    - records (list[Record]): List of records in namedtuple format.
    """
    display_records(records)
    index: int = int(input("Enter the index of the record to edit: "))
    
    if 0 <= index < len(records):
        last_name: str = input("Enter new last name: ")
        first_name: str = input("Enter new first name: ")
        surname: str = input("Enter new middle name: ")
        organization: str = input("Enter new organization: ")
        work_phone: str = input("Enter new work phone: ")
        personal_phone: str = input("Enter new personal phone: ")
        
        records[index] = Record(last_name, first_name, surname, organization, work_phone, personal_phone)
        print("Record edited successfully!")
    else:
        print("Invalid index.")

def search_records(records):
    """
    Search records by one or more keys and displays results

    Parameters:
    - records (list[Record]): List of records in namedtuple format.
    """
    search_term: str = input("Enter search term: ")
    found_records = [record for record in records if search_term.lower() in record.__str__().lower()]
    
    if found_records:
        display_records(found_records)
    else:
        print("No matching records found.")

def main():
    """
    Main function of the progtam. 
    Shows diplay that allows user to unteract with the program.
    """
    file_path: str = 'phone_book.txt'
    records = load_data(file_path)

    while True:
        print("\n1. Display records")
        print("2. Add record")
        print("3. Edit record")
        print("4. Search records")
        print("5. Save and exit")

        choice: str = input("Enter your choice (1-5): ")

        if choice == '1':
            display_records(records)
        elif choice == '2':
            add_record(records)
        elif choice == '3':
            edit_record(records)
        elif choice == '4':
            search_records(records)
        elif choice == '5':
            save_data(file_path, records)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
