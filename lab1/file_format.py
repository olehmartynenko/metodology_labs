from script import solve
from re import search
   
def validator(filename):
    pattern = r'^(-?\d+(\.\d+)?\s){2}-?\d+(\.\d+)?\n$'
    try:
        with open(filename, 'r') as file:
            line = file.read()
    except:
        print(f'File {filename} does not exist')
        return None
    matching = search(pattern, line)
    if matching:
        return matching.group()[:-2]
    else:
        print('Invalid file format')
        return None 