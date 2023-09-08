
def mode_lst(lst):
    frequency ={}

    for n in lst:
        if n in frequency:
            frequency[n] +=1
        else:
            frequency[n]=1
    
    max_freq = max(frequency.values())

    value_moda = [ k for k , v  in frequency.items() if v == max_freq]
    return (value_moda)



if __name__ == "__main__":
    lst = [4,6,2,6,9,0,6,4,5,3,6,6]
    print(mode_lst(lst))