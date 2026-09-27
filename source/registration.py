def register_user(username, age):
    if not isinstance(username, str):
        raise TypeError("Username must be a string")

    if not username:
        raise ValueError("Username cannot be empty")

    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if age < 18:
        raise ValueError("User must be at least 18")

    return f"User {username} registered successfully"
