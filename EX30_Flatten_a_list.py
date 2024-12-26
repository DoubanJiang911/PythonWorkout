def flatten(mylist):
    return [one_element
            for one_sublist in mylist
            for one_element in one_sublist]

def flatten_odd_ints(mylist):
    return [one_element
            for one_sublist in mylist
            for one_element in one_sublist
            if (type(one_element)==int or one_element.isdigit()) and int(one_element)%2==1]


print(flatten([[1,2], [3,4]]))

print(flatten_odd_ints([[1,2,3],['4','5','6'],[7,8,9]]))