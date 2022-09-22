USERS = [
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"},
]

def search_users(**kwargs):

    output_list = []
    if len(kwargs) < 1:
        print(USERS)

    elif len(kwargs) >= 1:

        #converts id input from string to int
        if "id" in kwargs:
            kwargs.update({"id": str(kwargs["id"])})

        for ind_dict in USERS:
            if kwargs.items() <= ind_dict.items():
                if ind_dict not in output_list:
                    output_list.append(ind_dict)
            else:
                for key, value in kwargs.items():
                    if type(value) == int:
                        if ind_dict[key] in range(value-1, value+2):
                            if ind_dict not in output_list:
                                output_list.append(ind_dict)
                    else: 
                        if ind_dict[key] == value or value in ind_dict[key]:
                            if ind_dict not in output_list:
                                output_list.append(ind_dict)

    return(output_list)    
    
print(search_users(id=5, name="Joe", age=30, occupation="Arc"))


