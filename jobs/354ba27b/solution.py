```python
"""
Student Name: Your Name
"""

# ============================
# BRONZE TIER FUNCTIONS
# ============================

def initialize_contacts() -> dict[str, dict[str, str | int]]:
    """
    Creates and returns a contact book dictionary with user input.
    Prompts for student ID, name, phone, email, grade for at least 3 contacts.
    """
    contact_book = {}
    
    while len(contact_book) < 3:
        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        grade = int(input("Enter grade: "))
        
        contact_book[student_id] = {
            "name": name,
            "phone": phone,
            "email": email,
            "grade": grade
        }
        
        print("Contact added!")
        
        if len(contact_book) < 3:
            add_another = input("Add another contact? (yes/no): ").lower()
            if add_another != 'yes':
                break
    
    return contact_book


def lookup_contact(contact_book: dict[str, dict[str, str | int]], student_id: str) -> dict[str, str | int] | None:
    """
    Looks up and displays a contact by student ID.
    Prints contact info or "Contact not found".
    """
    contact = contact_book.get(student_id)
    
    if contact:
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Grade: {contact['grade']}\n")
    else:
        print("Contact not found\n")
    
    return contact


# ============================
# SILVER TIER FUNCTIONS
# ============================

def validate_phone(phone: str) -> bool:
    """
    Validates phone number format "###-###-####".
    Returns True if valid, False if not.
    """
    return len(phone) == 12 and phone[3] == '-' and phone[7] == '-' and all(c.isdigit() for c in phone.replace('-', ''))


def validate_email(email: str) -> bool:
    """
    Validates email ends with "@dpcdsb.org".
    Returns True if valid, False if not.
    """
    return email.count('@') == 1 and email.endswith('@dpcdsb.org')


def add_contact(contact_book: dict[str, dict[str, str | int]], student_id: str, 
                name: str, phone: str, email: str, grade: int) -> bool:
    """
    Adds a new contact to the contact book with validation.
    Checks if student_id exists, validates grade, phone, and email.
    Prints status message and returns True if successful, False otherwise.
    """
    if student_id in contact_book:
        print("Student ID already exists")
        return False
    
    if grade not in [11, 12]:
        print("Error: Invalid grade. Must be 11 or 12.")
        return False
    
    if not validate_phone(phone):
        print("Error: Invalid phone number format")
        return False
    
    if not validate_email(email):
        print("Error: Invalid email format")
        return False
    
    contact_book[student_id] = {
        "name": name,
        "phone": phone,
        "email": email,
        "grade": grade
    }
    
    print("Contact added successfully!")
    return True


# ============================
# GOLD TIER FUNCTIONS
# ============================

def search_by_grade(contact_book: dict[str, dict[str, str | int]], grade: int) -> list[tuple[str, str]]:
    """
    Searches for all students in a specific grade.
    Returns sorted list of tuples (student_id, name).
    """
    results = [(sid, contact['name']) for sid, contact in contact_book.items() if contact['grade'] == grade]
    results.sort(key=lambda x: x[1])
    return results


def generate_statistics(contact_book: dict[str, dict[str, str | int]]) -> tuple[int, int, int, int, int, str]:
    """
    Generates statistics about the contact book.
    Returns tuple (total_contacts, grade9_count, grade10_count, grade11_count, grade12_count, common_area_code).
    """
    total_contacts = len(contact_book)
    grade_counts = {9: 0, 10: 0, 11: 0, 12: 0}
    
    area_codes = {}
    
    for contact in contact_book.values():
        grade_counts[contact['grade']] += 1
        area_code = contact['phone'][:3]
        if area_code in area_codes:
            area_codes[area_code] += 1
        else:
            area_codes[area_code] = 1
    
    most_common_area_code = max(area_codes, key=area_codes.get)
    
    return (total_contacts, grade_counts[9], grade_counts[10], grade_counts[11], grade_counts[12], most_common_area_code)


def display_menu() -> None:
    """
    Displays the menu options.
    """
    print("\n=== Student Contact System ===")
    print("1. Look up a contact")
    print("2. Add new contact")
    print("3. Search by grade")
    print("4. View statistics")
    print("5. Exit")


# ============================
# MAIN FUNCTION - ALL TIERS
# ============================

def main() -> None:
    """
    Main function - call your functions here to test them.
    For Bronze: Test initialize_contacts() and lookup_contact()
    For Silver: Also test validate functions and add_contact()
    For Gold: Implement the full interactive menu system
    """
    print("Welcome to the Student Contact System!")
    print("Let's initialize your contact book.\n")
    
    # Initialize the contact book with user input
    contact_book: dict[str, dict[str, str | int]] = initialize_contacts()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            student_id = input("Enter student ID to look up: ")
            lookup_contact(contact_book, student_id)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            grade = int(input("Enter grade: "))
            add_contact(contact_book, student_id, name, phone, email, grade)
        elif choice == '3':
            grade = int(input("Enter grade to search for: "))
            results = search_by_grade(contact_book, grade)
            print(f"\nStudents in grade {grade}:")
            for sid, name in results:
                print(f"{sid} - {name}")
        elif choice == '4':
            stats = generate_statistics(contact_book)
            print(f"\nTotal contacts: {stats[0]}")
            print(f"Grade 9 students: {stats[1]}")
            print(f"Grade 10 students: {stats[2]}")
            print(f"Grade 11 students: {stats[3]}")
            print(f"Grade 12 students: {stats[4]}")
            print(f"Most common area code: {stats[5]}\n")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
    
    print("\nThank you for using the Student Contact System!")


if __name__ == "__main__":
    main()
```