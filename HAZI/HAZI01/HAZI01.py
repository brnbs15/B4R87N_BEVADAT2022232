#Create a function that returns with a subsest of a list.
#The subset's starting and ending indexes should be set as input parameters (the list aswell).
#return type: list
#function name must be: subset
#input parameters: input_list,start_index,end_index

def subset(input_list,start_index,end_index)-> list:
    result=[]
    for  i in range(start_index,end_index):
        result.append(input_list[i])
    return result
subset([1,4,2,56,7],2,4)

#Create a function that returns every nth element of a list.
#return type: list
#function name must be: every_nth
#input parameters: input_list,step_size

def every_nth(input_list,step_size)-> list:
    nth=[]
    for i in range(step_size,len(input_list),2):
            nth.append(input_list[i])
    return nth
every_nth([1,4,2,56,7],2)

#Create a function that can decide whether a list contains unique values or not
#return type: bool
#function name must be: unique
#input parameters: input_list

def unique(input_list)-> bool:
    isunique=True
    for i in range(0,len(input_list)):
          for j in range(0,len(input_list)):
                 if input_list[i]==input_list[j] and j!=i :
                      isunique=False
    return isunique
unique([1,9,2,3,7])

#Create a function that can flatten a nested list ([[..],[..],..])
#return type: list
#fucntion name must be: flatten
#input parameters: input_list
def flatten(input_list : list) -> list:
    flatten_list = []

    for item in input_list:
        for x in item:
            flatten_list.append(x)
    return flatten_list

flatten([[1,2],[6,7],[3],[0,8]])
#Create a function that concatenates n lists
#return type: list
#function name must be: merge_lists
#input parameters: *args

def merge_lists(*args) -> list:
    concatenated=[]
    for i in args:
        for item in i:
             concatenated.append(item)
    return concatenated
merge_lists([1,2,34,5],[8,3,1,7,3],[2,45,6])


#Create a function that can reverse a list of tuples
#example [(1,2),...] => [(2,1),...]
#return type: list
#fucntion name must be: reverse_tuples
#input parameters: input_list

def reverse_tuples(input_list) -> list:
    reversed=[]
    for item in input_list:
        for  i in range(len(item)-1,-1,-1) :
            reversed.append(item[i])
    return reversed
reverse_tuples([(1,2,34,5),(8,3,1,7,3),(2,45,6)])

#Create a function that removes duplicates from a list
#return type: list
#fucntion name must be: remove_duplicates
#input parameters: input_list

def remove_duplicates(input_list)-> list:
    i=0
    while (i != len(input_list)):
        j=0
        while (j != len(input_list)):
                 if j==i:
                    j=j+1
                 elif input_list[i]==input_list[j]:
                    input_list.remove(input_list[j])
                 else:
                    j=j+1
        i=i+1
    return input_list
remove_duplicates([1,9,2,9,7])

#Create a function that transposes a nested list (matrix)
#return type: list
#function name must be: transpose
#input parameters: input_list

def transpose(input_list) ->list:
     result=[]
     for i in range(0,len(input_list)):
          row=[]
          for j in range(0,len(input_list[i])):
               row.append(input_list[j][i])
          result.append(row)
     return result
transpose([[1,2,3],[3,6,1],[8,4,5]])

#Create a function that can split a nested list into chunks
#chunk size is given by parameter
#return type: list
#function name must be: split_into_chunks
#input parameters: input_list,chunk_size
def split_into_chunks(input_list,chunk_size) ->list:
     result=[]
     for i in range(0,len(input_list),chunk_size):
        chunk=[]
        for j in range(i,i+chunk_size):
            if j < len(input_list):
                chunk.append(input_list[j])
        result.append(chunk)
split_into_chunks([1,2,3,3,6,1,8,4,5],2)

#Create a function that can merge n dictionaries
#return type: dictionary
#function name must be: merge_dicts
#input parameters: *dict

def merge_dicts(*dict) -> dict:
    result = {}
    for i in dict:
        result = result | i
    return result

#Create a function that receives a list of integers and sort them by parity
#and returns with a dictionary like this: {"even":[...],"odd":[...]}
#return type: dict
#function name must be: by_parity
#input parameters: input_list
def by_parity(input_list) -> dict:
    even = []
    odd = []
    for i in input_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return {"even" : even, "odd" : odd}
by_parity([2,3,6,1,3,5,8])

#Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
#and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
#in short calculates the mean of the values key wise
#return type: dict
#function name must be: mean_key_value
#input parameters: input_dict

def mean_key_value(input_dict : dict) -> dict:
    result = {}
    for key, value in input_dict.items():
        mean = 0
        for i in value:
            mean = mean + i
        result[key] = mean / len(value)
    return result
