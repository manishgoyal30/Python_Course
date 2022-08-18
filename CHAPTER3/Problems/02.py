letter = '''Dear <|name|>
            You are Selected!
            <|Date|>'''

name = input("Enter your name: ")
date = input("Enter the Date: ")

letter = letter.replace("<|name|>", name)
letter = letter.replace("<|Date|>", date)

print(letter)