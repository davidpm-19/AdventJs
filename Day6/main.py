def inBox(box):
    for i in range(1, len(box) - 1):
        row = box[i]
        if '*' in row:
            index = row.index('*')
            if index > 0 and index < len(row) - 1:
                return True
    return False