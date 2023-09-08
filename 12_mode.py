### 12 Mode
#Write a function that finds the mode in a list of numbers. The mode is the number that appears most frequently.
import statistics

def mode_lst(lst):
    moda = statistics.mode(lst)
    return moda 






if __name__ == "__main__":
    lst = [9,9,3,1,2,4,6,7,7,8,8,9]
    print(mode_lst(lst))