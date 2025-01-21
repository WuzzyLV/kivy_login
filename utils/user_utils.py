import csv
import os
from uuid import uuid4

# Path to the CSV file
USERS_FILE = 'data/users.csv'


def get_user_by_uuid(user_uuid: str):
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter='\t')
                for row in reader:
                    if row['uuid'] == user_uuid:
                        return row
        except Exception as e:
            print(f"Error reading users file: {e}")
    return None

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

def create_user(username: str, password: str):
    if get_user(username):
        raise ValueError("User with this username already exists.")

    user_uuid = str(uuid4())
    new_user = {
        'uuid': user_uuid,
        'username': username,
        'password': password
    }

    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'a', encoding='utf-8', newline='') as file:
                fieldnames = ['uuid', 'username', 'password']
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
                writer.writerow(new_user)
                print(f"Created new user {username}")
        except Exception as e:
            print(f"Error writing to users file: {e}")
    else:
        try:
            with open(USERS_FILE, 'w', encoding='utf-8', newline='') as file:
                fieldnames = ['uuid', 'username', 'password']
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
                writer.writeheader()
                writer.writerow(new_user)
                print(f"Created new user {username}")
        except Exception as e:
            print(f"Error creating users file: {e}")


def change_password(user_uuid: str, new_password: str):
    """Change the password of a user identified by their UUID."""
    if os.path.exists(USERS_FILE):
        try:
            users_data = []
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter='\t')
                fieldnames = reader.fieldnames
                if fieldnames is None or 'uuid' not in fieldnames or 'username' not in fieldnames or 'password' not in fieldnames:
                    raise ValueError("Invalid CSV format. Missing 'uuid', 'username' or 'password' columns.")
                
                user_found = False
                for row in reader:
                    if row['uuid'] == user_uuid:
                        row['password'] = new_password
                        user_found = True
                    users_data.append(row)

            if user_found:
                with open(USERS_FILE, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
                    writer.writeheader()
                    writer.writerows(users_data)
                return True
            else:
                print(f"No user found with UUID {user_uuid}")
                return False
        except Exception as e:
            print(f"Error updating password: {e}")
    return False


#change username
def change_username(user_uuid: str, new_username: str):
    """Change the username of a user identified by their UUID."""
    if os.path.exists(USERS_FILE):
        try:
            users_data = []
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter='\t')
                fieldnames = reader.fieldnames
                if fieldnames is None or 'uuid' not in fieldnames or 'username' not in fieldnames or 'password' not in fieldnames:
                    raise ValueError("Invalid CSV format. Missing 'uuid', 'username' or 'password' columns.")
                
                user_found = False
                for row in reader:
                    if row['uuid'] == user_uuid:
                        row['username'] = new_username
                        user_found = True
                    users_data.append(row)

            if user_found:
                with open(USERS_FILE, 'w', encoding='utf-8', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
                    writer.writeheader()
                    writer.writerows(users_data)
                return True
            else:
                print(f"No user found with UUID {user_uuid}")
                return False
        except Exception as e:
            print(f"Error updating username: {e}")
    return False