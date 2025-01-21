import os
import csv
import uuid
from datetime import datetime

# Base directory where user notes will be stored
USER_DATA_DIR = 'data/user_data'

def ensure_user_notes_file_exists(user_uuid: str):
    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)

    # Define the path for the user's notes CSV file
    notes_file_path = os.path.join(USER_DATA_DIR, f'{user_uuid}_notes.csv')

    # Check if the CSV file exists, if not, create it with headers
    if not os.path.exists(notes_file_path):
        try:
            # Create and write header row to the CSV file
            with open(notes_file_path, 'w', encoding='utf-8', newline='') as file:
                fieldnames = ['uuid', 'note', 'color', 'created_at', 'category']
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                print(f"Created new notes file for user {user_uuid}")
        except Exception as e:
            print(f"Error creating notes file for user {user_uuid}: {e}")

    return notes_file_path

def add_note_to_user(user_uuid: str, note: str, color: str, category: str):
    notes_file_path = ensure_user_notes_file_exists(user_uuid)  

    # Generate a new UUID for the note and get the current timestamp
    note_uuid = str(uuid.uuid4())
    created_at = datetime.now().isoformat()

    new_note = {
        'uuid': note_uuid,
        'note': note,
        'color': color,
        'created_at': created_at,
        'category': category
    }

    # Add the new note to the user's notes CSV file
    try:
        with open(notes_file_path, 'a', encoding='utf-8', newline='') as file:
            fieldnames = ['uuid', 'note', 'color', 'created_at', 'category']
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
            writer.writerow(new_note)
            print(f"Added new note for user {user_uuid}")
    except Exception as e:
        print(f"Error adding note for user {user_uuid}: {e}")

