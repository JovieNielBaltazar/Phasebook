
USERS = [
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"},
]

def search_users(**kwargs):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """


    print("test")
    if len(kwargs) < 1:
        print(USERS)

    elif len(kwargs) >= 1:
        if "id" in kwargs:
            kwargs.update({"id": str(kwargs["id"])})
            
        for ind_dict in USERS:
            if kwargs.items() <= ind_dict.items():
                print(ind_dict)
            else:
                for key, value in kwargs.items():
                    if type(value) == int:
                        if ind_dict[key] in range(value-1, value+2):
                            print(ind_dict)
                    else: 
                        if ind_dict[key] == value or value in ind_dict[key]:
                            print(ind_dict)

    #if len(kwargs) >= 1:
    #    if "id" in kwargs:
     #       kwargs.update({"id": str(kwargs["id"])})
      #  
       # for pair in USERS:
        #    if kwargs.items() <= pair.items():
         #       print(pair)
         #   elif pair["age"] in range(kwargs["age"]-1, kwargs["age"]+2):
          #      print(pair)
           # elif kwargs["occupation"].lower() in pair["occupation"].lower():
            #    print(pair)
        ##for pair in USERS:
            #if kwargs.items() <= pair.items():
                #print(pair)
            #elif kwargs["name"] in pair["name"] or kwargs["id"] == pair["id"] or kwargs["occupation"] in pair["occupation"]:
                #print(pair)
        #for pair in USERS:
        #    if pair["age"] in range(kwargs["age"]-1, kwargs["age"]+2):
        #        print(pair)
        #for pair in USERS:
        #    if kwargs["occupation"].lower() in pair["occupation"].lower():
        #        print(pair)

        
    


    
search_users(id=5, name="Joe", age=30, occupation="Arc")



    