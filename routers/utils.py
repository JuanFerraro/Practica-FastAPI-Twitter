import json

# Function: READ FILE
def read_file(path: str):
    """**READ FILE**

    *Function to read a file json*

    Args:
        path (_str_): _This is the route to the file that is going to be read_

    Returns:
        _list_: _Returns a list with the content of a json file _
    """
    with open(f'{path}', 'r', encoding="utf-8") as file:
        lista = json.load(file) # Convierte json a lista
    return lista

# Function: WRITE IN FILE
def write_file(list: list, path: str):
    """**WRITE IN FILE**

    Args:
        list (list): _This is the list that will be added to the json file_
        path (str): _This is the route of the json file_
    """
    with open(f'{path}', 'w', encoding="utf-8") as file:
        json.dump(list, file, indent=4)

# Function: FIND IN FILE
def find_in_file(list: list, key: str, value: str):
    """**FIND IN FILE**

    Args:
        list (list): _description_
        id (str): _description_

    Returns:
        _type_: _description_
    """
    found = next((something for something in list if something[f'{key}'] == value), None)
    if found != None:
        return found
    else: 
        return False