#!/usr/bin/python3

"""
Defining the MyList class
"""


class MyList(list):
    """
    inheriting from list class and also defining the print_sorted method
    """
   
    def print_sorted(self):
        sorted_list = []
        for num in self:
            if not len(sorted_list):
                sorted_list.append(num)
                continue
            for index, entry in enumerate(sorted_list):
                if num < entry and num > sorted_list[index + 1]:
                    sorted_list.insert(index+1, nu
                    
        print(sorted_list)
