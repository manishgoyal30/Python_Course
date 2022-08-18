def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Manish is good      "
n = remove_and_split(this, "Manish")
print(n)
