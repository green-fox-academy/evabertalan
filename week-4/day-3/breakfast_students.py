students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

def gold_candy(kid):
    rich_mother=0
    for i in kid:
        if i["candies"]>3:
            rich_mother+=1
    return(rich_mother)

print(gold_candy(students))





def is_rich(bab):
    return bab["candies"]>4

def filter_gold_candy(tomi):
    return len(list(filter(is_rich, tomi)))

print(filter_gold_candy(students))




def rich_kids_ever(fellas):
    return len(list(filter(lambda x: x["candies"]>4, fellas)))

print(rich_kids_ever(students))
