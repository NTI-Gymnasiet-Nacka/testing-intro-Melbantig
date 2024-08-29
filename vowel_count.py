# Vokalräkning
vowels=["a","e","i","o","u","y","å","ä","ö"]

def main():
    total_vowels=0
    word=str(input(""))
    
    for char in word:
        if char in vowels:
            total_vowels+=1
    
    print(total_vowels)
            
if __name__ == "__main__":
    main()
