## Working with Data
### 10 Average
#Write a function that takes a list of numbers and calculates their average.

def average (lst):
    average_lst = sum(lst) / len(lst)
    return (average_lst)




if __name__ == '__main__':
    lst = [29, 87, 56 , 77 , 53, 23]
    print(average(lst))
