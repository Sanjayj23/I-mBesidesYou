import json
import re

def get_course_code(course_name_full):
    """Extracts a course code like 'CE214' from '... (CE214)'."""
    match = re.search(r'\(([A-Z]{2,3}\d{3,4}[A-Z]?)\)', course_name_full)
    if match:
        return match.group(1)
    
    match_eso = re.search(r'([A-Z]{2,3}\d{3,4}[A-Z]?)', course_name_full)
    if match_eso:
        return match_eso.group(1)
    return None

# --- 1. Load both data files ---
try:
    with open('schedule_data.json', 'r', encoding='utf-8') as f:
        schedule_data = json.load(f)
    print(f"Loaded {len(schedule_data)} courses from schedule_data.json")

    with open('grading_data.json', 'r', encoding='utf-8') as f:
        grading_data = json.load(f)
    print(f"Loaded {len(grading_data)} grading entries from grading_data.json")

except FileNotFoundError as e:
    print(f"Error: {e.filename} not found.")
    print("Please make sure 'schedule_data.json' and 'grading_data.json' are in the same folder.")
    exit()

final_database = []

# --- 2. Loop, Extract Code, and Merge ---
for course in schedule_data:
    course_code = get_course_code(course['CourseName'])
    
    if course_code:
        # Check for the code and its variations (e.g., CE371 vs CE371A)
        grading_info = grading_data.get(course_code)
        
        if not grading_info and course_code.endswith('A'):
             grading_info = grading_data.get(course_code[:-1]) # Try without 'A'
        elif not grading_info and not course_code.endswith('A'):
             grading_info = grading_data.get(course_code + 'A') # Try with 'A'

        if grading_info:
            course['Grading'] = grading_info
        else:
            course['Grading'] = {"Analysis": "No historical grading data found.", "History": []}
    else:
        print(f"Warning: Could not extract course code from {course['CourseName']}")
        course['Grading'] = {"Analysis": "Error parsing course code.", "History": []}

    final_database.append(course)

# --- 3. Save the final merged database ---
try:
    with open('final_database.json', 'w', encoding='utf-8') as f:
        json.dump(final_database, f, indent=2, ensure_ascii=False)
    print(f"\nSuccess! Merged data for {len(final_database)} courses into 'final_database.json'.")

except Exception as e:
    print(f"An error occurred while writing the file: {e}")