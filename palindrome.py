# Palindrome
def main():
    word=str(input(''))
    if word == word[::-1]:
        print('True')
    else:
        print('False')
    
if __name__ == "__main__":
    main()
