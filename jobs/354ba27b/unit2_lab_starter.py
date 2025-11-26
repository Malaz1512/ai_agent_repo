"""
TODO: Add your header comments here.
"""

# ============================
# BRONZE TIER FUNCTIONS
# ============================

def initialize_contacts() -> dict[str, dict[str, str | int]]:
    """
    Creates and returns a contact book dictionary with user input.
    Prompts for student ID, name, phone, email, grade for at least 3 contacts.
    """
    # TODO: Create empty dictionary, use loop to get at least 3 contacts from user, return dictionary
    
    pass


def lookup_contact(contact_book: dict[str, dict[str, str | int]], student_id: str) -> dict[str, str | int] | None:
    """
    Looks up and displays a contact by student ID.
    Prints contact info or "Contact not found".
    """
    # TODO: Use .get() to retrieve contact, print info if found or error message if not
    
    pass


# ============================
# SILVER TIER FUNCTIONS
# ============================

def validate_phone(phone: str) -> bool:
    """
    TODO: add docstring comments, delete this line once done.
    """
    # TODO: Check length is 12, dashes at index 3 and 7, all other chars are digits
    
    pass


def validate_email(email: str) -> bool:
    """
    TODO: add docstring comments, delete this line once done.
    """
    # TODO: Check for exactly one "@" and ends with "@school.com"
    
    pass


def add_contact(contact_book: dict[str, dict[str, str | int]], student_id: str, 
                name: str, phone: str, email: str, grade: int) -> bool:
    """
    Adds a new contact to the contact book with validation.
    Checks if student_id exists, validates grade, phone, and email.
    Prints status message and returns True if successful, False otherwise.
    """
    # TODO: Check if student_id exists, validate grade (11 or 12), validate phone and email, add contact if all pass
    
    pass


# ============================
# GOLD TIER FUNCTIONS
# ============================

def search_by_grade(contact_book: dict[str, dict[str, str | int]], grade: int) -> list[tuple[str, str]]:
    """
    Searches for all students in a specific grade.
    Returns sorted list of tuples (student_id, name).
    """
    # TODO: Loop through contacts, find matching grade, add (student_id, name) tuples to list, sort by name, return list
    
    pass


def generate_statistics(contact_book: dict[str, dict[str, str | int]]) -> tuple[int, int, int, int, int, str]:
    """
    Generates statistics about the contact book.
    Returns tuple (total_contacts, grade11_count, grade12_count, common_area_code).
    """
    # TODO: Count total contacts, count grade 9, 10, 11 and 12 students, find most common area code, 
    # then, return as tuple
    
    pass


def display_menu() -> None:
    """
    TODO: add docstring comments, delete this line once done.
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
    
    # BRONZE TIER: Test your functions here
    # TODO: Call lookup_contact() to test looking up a student
    
    # SILVER TIER: Test your functions here
    # TODO: Test validate_phone() and validate_email(), then test add_contact()
    
    # GOLD TIER: Implement interactive menu
    # TODO: Create while loop with menu, handle user choices (1-5), call appropriate functions
    
    print("\nThank you for using the Student Contact System!")


if __name__ == "__main__":
    main()
