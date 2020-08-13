def find_product(lst):
    result = []
    left = 1

    for i in range(len(lst)):
        current_product = 1

        for el in lst[i+1:]:
            current_product *= el 
        
        result.append(current_product * left)

        left *= lst[i]

    print(result)
    return result



find_product([1,2,3,4,5,0])