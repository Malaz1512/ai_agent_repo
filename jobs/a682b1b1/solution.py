```python
"""
Created by: Your Name
Date: YYYY-MM-DD
ICS4U Lab: Student Contact System - Strings, Lists, Tuples & Dictionaries
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
    for _ in range(3):
        student_id = input("Enter student ID: ").strip()
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        grade = int(input("Enter grade: ").strip())
        
        contact_book[student_id] = {
            "name": name,
            "phone": phone,
            "email": email,
            "grade": grade
        }
        
        print("Contact added!")
    
    return contact_book


def lookup_contact(contact_book: dict[str, dict[str, str | int]], student_id: str) -> dict[str, str | int] | None:
    """
    Looks up and displays a contact by student ID.
    Prints contact info or "Contact not found".
    """
    contact = contact_book.get(student_id)
    if contact:
        print(f"Student ID: {student_id}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Grade: {contact['grade']}")
        return contact
    else:
        print("Contact not found")
        return None


# ============================
# SILVER TIER FUNCTIONS
# ============================

def validate_phone(phone: str) -> bool:
    """
    Validates if the phone number is in format "###-###-####".
    Returns True if valid, False otherwise.
    """
    if len(phone) != 12 or phone[3] != '-' or phone[7] != '-':
        return False
    if not all(char.isdigit() for char in (phone[:3] + phone[4:7] + phone[8:])):
        return False
    return True


def validate_email(email: str) -> bool:
    """
    Validates if the email contains exactly one "@" symbol and ends with "@dpcdsb.org".
    Returns True if valid, False otherwise.
    """
    if email.count('@') != 1 or not email.endswith('@dpcdsb.org'):
        return False
    return True


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
    
    if grade not in (11, 12):
        print("Error: Grade must be 11 or 12")
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
    results = [(sid, info["name"]) for sid, info in contact_book.items() if info["grade"] == grade]
    return sorted(results, key=lambda x: x[1])


def generate_statistics(contact_book: dict[str, dict[str, str | int]]) -> tuple[int, int, int, int, int, str]:
    """
    Generates statistics about the contact book.
    Returns tuple (total_contacts, grade9_count, grade10_count, grade11_count, grade12_count, common_area_code).
    """
    total_contacts = len(contact_book)
    grade_counts = {9: 0, 10: 0, 11: 0, 12: 0}
    
    area_codes = {}
    for info in contact_book.values():
        grade_counts[info["grade"]] += 1
        area_code = info["phone"][:3]
        if area_code in area_codes:
            area_codes[area_code] += 1
        else:
            area_codes[area_code] = 1
    
    common_area_code = max(area_codes, key=area_codes.get)
    
    return (
        total_contacts,
        grade_counts[9],
        grade_counts[10],
        grade_counts[11],
        grade_counts[12],
        common_area_code
    )


def display_menu() -> None:
    """
    Displays the menu options for the interactive system.
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
    contact_book = initialize_contacts()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            student_id = input("Enter student ID to look up: ").strip()
            lookup_contact(contact_book, student_id)
        
        elif choice == '2':
            student_id = input("Enter student ID: ").strip()
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            grade = int(input("Enter grade: ").strip())
            add_contact(contact_book, student_id, name, phone, email, grade)
        
        elif choice == '3':
            grade = int(input("Enter grade to search for: ").strip())
            results = search_by_grade(contact_book, grade)
            if results:
                print(f"Students in Grade {grade}:")
                for sid, name in results:
                    print(f"{sid}: {name}")
            else:
                print("No students found in that grade.")
        
        elif choice == '4':
            stats = generate_statistics(contact_book)
            total_contacts, grade9_count, grade10_count, grade11_count, grade12_count, common_area_code = stats
            print(f"Total Contacts: {total_contacts}")
            print(f"Grade 9 Count: {grade9_count}")
            print(f"Grade 10 Count: {grade10_count}")
            print(f"Grade 11 Count: {grade11_count}")
            print(f"Grade 12 Count: {grade12_count}")
            print(f"Most Common Area Code: {common_area_code}")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    print("\nThank you for using the Student Contact System!")


if __name__ == "__main__":
    main()
```