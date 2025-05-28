# პირველი
def length(lst):
    return len(lst)


# მეორე
def new_list(original_list):
    copied_list = []
    for item in original_list:
        copied_list.append(item)
    return copied_list

# მესამე
def double_length(s):
    return len(s) * 2


# მეოთხე
def insert_guram(lst):
    lst.insert(2, "გურამი")
    return lst

# მეხუთე
def remove_second_index(lst):
    if len(lst) > 2:
        lst.pop(2)
    return lst
