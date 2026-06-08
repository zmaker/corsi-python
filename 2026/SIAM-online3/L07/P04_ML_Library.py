def renameCol(row, old_name, new_name):
    val = row.pop(old_name)
    row[new_name] = val.strip()