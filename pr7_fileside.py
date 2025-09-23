
def new_file(name):
    with open(name, "x", encoding="utf-8") as f:
        f.write("")
    return True

def file_write(name, data):
    with open(name, "w", encoding="utf-8") as f:
        f.write(data)
    return True

def file_read(name):
    with open(name, "r", encoding="utf-8") as f:
        return f.read()

def file_append(name, data):
    with open(name, "a", encoding="utf-8") as f:
        f.write(data)
    return True
