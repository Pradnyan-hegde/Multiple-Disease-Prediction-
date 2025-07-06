# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 19:03:11 2024

@author: sanni
"""

import json
import os

# File to store user credentials
USER_CREDENTIALS_FILE = "users.json"

# Load users from the JSON file
def load_users():
    if os.path.exists(USER_CREDENTIALS_FILE):
        with open(USER_CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save users to the JSON file
def save_users(users):
    with open(USER_CREDENTIALS_FILE, "w") as file:
        json.dump(users, file)

# Define authentication functions
def create_account(username, password):
    users = load_users()
    if username in users:
        return False  # Username already exists
    users[username] = password
    save_users(users)  # Save to file
    return True

def login(username, password):
    users = load_users()
    if username in users and users[username] == password:
        return True
    return False

def logout():
    return False, None  # Reset authentication state
