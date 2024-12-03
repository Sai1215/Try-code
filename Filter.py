def odd_even_sum(my_list):
    from functools import reduce
    odd_list = list(filter(lambda x: x % 2 == 1, my_list))
    even_list = list(filter(lambda x: x % 2 == 0, my_list))
    
    print("odd_list:",odd_list)
    print("even_list",even_list)