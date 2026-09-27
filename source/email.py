def is_valid_email(email: str) -> bool:
    """
    Returns True if an email is valid, False otherwise.
    Rules:
    - Must be a string
    - Must contain exactly one '@'
    - Must contain a '.' after the '@'
    """
    if not isinstance(email, str):
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if not username or not domain:
        return False

    if "." not in domain or domain.startswith(".") or domain.endswith("."):
        return False

    return True
