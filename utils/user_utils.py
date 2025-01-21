import csv
import os

# Path to the CSV file
USERS_FILE = 'data/users.csv'

def get_user(username: str):
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter='\t')
                for row in reader:
                    if row['username'] == username:
                        return row
        except Exception as e:
            print(f"Error reading users file: {e}")
    return None

def change_password(username: str, new_password: str) -> bool:
    if os.path.exists(USERS_FILE):
        try:
            users_data = []
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter='\t')
                fieldnames = reader.fieldnames
                if fieldnames is None or 'username' not in fieldnames or 'password' not in fieldnames:
                    raise ValueError("Invalid CSV format. Missing 'username' or 'password' columns.")
                
                for row in reader:
                    if row['username'] == username:
                        row['password'] = new_password
                    users_data.append(row)

            with open(USERS_FILE, 'w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                writer.writerows(users_data)
            
            return True
        except Exception as e:
            print(f"Error updating password: {e}")
    return False
