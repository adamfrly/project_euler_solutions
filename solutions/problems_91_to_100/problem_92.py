# How many starting numbers below ten million will arrive at 89? Given you continually add the sqaures of the digits of each succesive number.

def square_of_digits(n):
    digits = list(str(n))
    return sum([int(x) ** 2 for x in digits]) 

eighty_nines = {89:True, 1:False}

def one_or_89(i):
    orig = i
    prev = None
    while prev != 1 or prev != 89:
        i = int("".join(sorted(str(square_of_digits(i)))))
        try:
            if eighty_nines[i] == True:
                eighty_nines[orig] = True
                return True
            if eighty_nines[i] == False:
                eighty_nines[orig] = False
                return False
        except Exception as e:
            pass
        prev = i
    if i == 89:
        eighty_nines[orig] = True
        return True
    elif i == 1:
        eighty_nines[orig] = False
        return False
    
print(len([x for x in map(one_or_89, list(range(2, 10000000))) if x]))
