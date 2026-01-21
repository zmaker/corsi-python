import re

EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def email_valida(email):
    if not email:
        return False
    return bool(EMAIL_REGEX.match(email))

def renameCol(row, old_name, new_name):
    valore = row[old_name]
    row.pop(old_name)
    row[new_name] = valore