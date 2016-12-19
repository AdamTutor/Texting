def email_is_valid(email):
    return "@" in email and ".com" in email

def username_is_valid(username):
    return len(username) >= 3

def password_is_valid(password):
    return len(password) >= 5

def password_confirm(password, password_confirm):
    return password == password_confirm
