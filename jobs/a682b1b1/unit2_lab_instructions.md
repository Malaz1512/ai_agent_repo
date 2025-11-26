# ICS4U Lab: Student Contact System - Strings, Lists, Tuples & Dictionaries

## Overview
In this lab, you will create a contact management system for your school. The system needs to store student information, validate data, and provide various lookup and analysis features. You will practice working with strings, lists, tuples, and dictionaries. Each tier builds upon the previous one.

## Bronze Tier [MAX 65%]:

### Requirements

**Task 1: Initialize the Contact Book**

Create a function `initialize_contacts()` that:
- Creates an empty dictionary called `contact_book`
- Uses a loop to ask the user to input information for **at least 3 student contacts**
- For each contact, prompt for:
  - Student ID (e.g., "S001")
  - Name
  - Phone number
  - Email
  - Grade
- Store each contact as a dictionary with keys: "name", "phone", "email", "grade"
- Add each contact to the contact_book using the student ID as the key
- Returns the contact_book dictionary

**Hint:** You can use a while loop and ask "Add another contact? (yes/no)" or use a for loop with `range(3)` for exactly 3 contacts.

**Task 2: Look Up and Display Contact**

Create a function `lookup_contact(contact_book, student_id)` that:
- Takes the contact_book dictionary and a student_id string
- Uses `.get()` method to safely retrieve the contact
- If found, prints the contact information in a readable format with all fields
- If not found, prints "Contact not found"
- Returns the contact dictionary if found, or None if not found

### Sample Output
```
=== Initializing Contact Book ===
Enter student ID: S001
Enter name: Alice Smith
Enter phone: 416-555-0123
Enter email: alice@dpcdsb.org
Enter grade: 12
Contact added!

Enter student ID: S002
Enter name: Bob Jones
Enter phone: 416-555-0124
Enter email: bob@dpcdsb.org
Enter grade: 11
Contact added!

Enter student ID: S003
Enter name: Cindy Applewood
Enter phone: 416-999-0000
Enter email: cindy@dpcdsb.org
Enter grade: 10
Contact added!

Add another contact? (yes/no): no

=== Looking Up Contact ===
Enter student ID to look up: S001

Student ID: S001
Name: Alice Smith
Phone: 416-555-0123
Email: alice@dpcdsb.org
Grade: 12
```

## Silver Tier [MAX 85%]:

### Requirements

**Task 3: Phone and Email Validation**

Create two validation functions:

**Function 1:** `validate_phone(phone)` that:
- Checks if the phone number is in format "###-###-####" (10 digits with dashes)
- Use string methods to validate:
  - Length is exactly 12 characters
  - Characters at positions 3 and 7 are dashes
  - All other characters are digits (use `.isdigit()`)
- Returns `True` if valid, `False` if not

**Function 2:** `validate_email(email)` that:
- Checks if email contains exactly one "@" symbol (hint: use `.count()`)
- Checks if email ends with "@dpcdsb.org" (hint: use `.endswith()`)
- Returns `True` if valid, `False` if not

**Task 4: Add New Contact with Validation**

Create a function `add_contact(contact_book, student_id, name, phone, email, grade)` that:
- Checks if the student_id already exists (use `in` operator)
- If it exists, print "Student ID already exists" and return False
- Checks if grade is 11 or 12 (print error message if not)
- Uses `validate_phone()` and `validate_email()` to validate input
- If all checks pass, adds the new contact and prints "Contact added successfully"
- Returns True if successful, False otherwise

### Sample Output
```
=== Testing Validation ===
Testing phone: 416-555-1234
Valid? True

Testing phone: 4165551234
Valid? False

Testing email: test@dpcdsb.org
Valid? True

Testing email: test@gmail.com
Valid? False

=== Adding New Contact ===
Adding contact ...
Error: Invalid phone number format
Contact not added.

Adding contact ...
Contact added successfully!
```

## Gold Tier [Max 100%] - No teacher support at this point, good luck!

### Requirements

**Task 5: Search by Grade**

Create a function `search_by_grade(contact_book, grade)` that:
- Takes a grade level (9 to 12)
- Returns a list of tuples containing (student_id, name) for all students in that grade
- Sort the list alphabetically by name before returning
- If no students found, return an empty list

**Task 6: Generate Contact Statistics**

Create a function `generate_statistics(contact_book)` that:
- Calculates and returns a tuple containing (in this order):
  1. Total number of contacts (int)
  2. Number of Grade 9 students (int)
  3. Number of Grade 10 students (int)
  4. Number of Grade 11 students (int)
  5. Number of Grade 12 students (int)
  6. Most common area code from phone numbers (string of first 3 digits)
- Use tuple unpacking when calling this function in `main()` to display results

**Task 7: Create Interactive Menu System**

Create a function `display_menu()` that displays the menu options, and update your `main()` function to run an interactive system:

**The menu should display:**
```
=== Student Contact System ===
1. Look up a contact
2. Add new contact
3. Search by grade
4. View statistics
5. Exit
Enter your choice (1-5):
```

**Your `main()` function should:**
- Call `initialize_contacts()` at the start (with user input)
- Use a while loop to continuously show the menu until user chooses to exit
- Use if/elif statements to call the appropriate function based on user choice
- Handle invalid menu choices gracefully
- For each option, prompt for necessary inputs and display results

### Sample Output
```
=== Student Contact System ===
1. Look up a contact
2. Add new contact
3. Search by grade
4. View statistics
5. Exit
Enter your choice (1-5): 4

=== Contact Statistics ===
Total contacts: 8
Grade 9 students: 0
Grade 10 students: 0
Grade 11 students: 3
Grade 12 students: 5
Most common area code: 416

=== Student Contact System ===
1. Look up a contact
2. Add new contact
3. Search by grade
4. View statistics
5. Exit
Enter your choice (1-5): 3
Enter grade (9 to 12): 11
Grade 11 students:
  S002: Bob Jones
  S004: Diana Lee

=== Student Contact System ===
1. Look up a contact
2. Add new contact
3. Search by grade
4. View statistics
5. Exit
Enter your choice (1-5): 5
Thank you for using the Student Contact System!
```

## Reminders:
* Do not forget header comments with your name
* Use comments to explain your code
* Start with Bronze. Then if you have time, build your way to Silver/Gold!
* All tiers should call their functions in the `main()` function

## Submission Instructions
- Submit your .py file as unit2_lab_tier.py (e.g., unit2_lab_gold.py)