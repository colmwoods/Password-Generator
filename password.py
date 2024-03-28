import random
import string

def make(characters):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    others = "~`!@#$%^&*()_-+={[}]|:;""'<,>.?/"  
    
    others = random.choice(others) # This Will Make Sure That Their Is 1 Or More Symbols In The Generated Passcode # 
    
    
    remaining = characters - 1
    ans = ''.join(random.choice(uppercase + lowercase + numbers) for _ in range(remaining))

    position = random.randint(0, remaining)
    ans = ans[:position] + others + ans[position:]


    print("Your New Password Is: ", ans)

    value = list(ans)
    random.shuffle(value)
    ans = ''.join(value)

    return ans
try:
    while True:
        characters = int(input("How many characters would you like your password to be: "))
        ans = make(characters)
        break


except ValueError:
    while True:
        try:
            characters = int(input("Needs to be a number. How many characters would you like your password to be: "))
            ans = make(characters)
            break
        except ValueError:
            print("Please Listen")