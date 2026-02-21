"""
Create a dictionary representing a user (keys: username,
department, is_admin). Write an if statement that prints "High Risk" if
is_admin is True.

"""

# Step 1. Create user
user = {"username": "Shadow", "department": "IT", "is_admin": True}

# Step 2. check if is_admin is true
if user["is_admin"]:
    print("High Risk")
else:
    print("Low Risk")
