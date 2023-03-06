greeting="Hello world!"
print(greeting)

for letter in greeting:
    print(letter)

def greeting_method(greeting):
    print(greeting)


#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

def contains_odd(input_list : list) -> bool:
    oddnum=False
    i = 0
    while(i<len(input_list) and input_list[i]%2==0):
        i=i+1
    if(i<len(input_list)):
        oddnum=True
    return oddnum

#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list
def is_odd(input_list : list) -> list:
    masked_list = []
    for item in input_list:
        if item % 2 == 0:
            masked_list.append(False)
        else:
            masked_list.append(True)
    return masked_list


#Create a function that accpects 2 lists of integers and returns their element wise sum. 
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2
def element_wise_sum(input_list1 : list, input_list2 : list) -> list:
    i = 0
    j = 0
    sum_list = []
    while( i < len(input_list1) and j < len(input_list2)):
        sum_list.append(input_list1[i]+input_list2[j])
        i = i + 1
        j = j + 1
    while(i < len(input_list1)):
        sum_list.append(input_list1[i])
        i = i + 1
    while(j < len(input_list2)):
        sum_list.append(input_list2[j])
        j = j + 1
    return sum_list


#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict
def dict_to_list(input_dict : dict) -> list:
    output_list=[]
    for key,value in input_dict.items():
        output_list.append((key,value))
    return output_list
     