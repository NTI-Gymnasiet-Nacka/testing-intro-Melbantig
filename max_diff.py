# Största skillnad
number_list=[]
def main():
    numbers=(input("").split(','))
    for u in numbers:
        number_list.append(int(u))
    max_diff=max(number_list) - min(number_list)
    print(max_diff)
    
    

if __name__ == "__main__":
    main()
