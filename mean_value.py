# Medelvärde
def main():
    str_numbers=input("").split(',')

    total_numbers=len(str_numbers)

    numbers=[int(i) for i in str_numbers]

    mean_value=sum(numbers)/total_numbers

    print(mean_value)

if __name__ == "__main__":
    main()
