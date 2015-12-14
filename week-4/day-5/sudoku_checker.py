def is_complete(numbers):
    k=sum(numbers)
    if len(numbers) != 9:
        return False
    if k == 45:
        return True
