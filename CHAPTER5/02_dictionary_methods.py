myDict = {
    "fast": "In a Quick Manner",
    "Harry": "A coder",
    "Marks": [1,2,5],
    "anotherdist": {'harry': 'Player'},
    1:2
}

# Dictonary Methods

print(list(myDict.keys())) # Print the keys of the dictionary
print(list(myDict.values())) # Prints the values of the dictionary
print(myDict.items()) #print the (keys, value) for all the components of dictionary
print(myDict)

  ### Updates function 
updateDict = {
    "Lavish": "Friend"
}
myDict.update(updateDict) #update the dictionary ny adding key values pairs from uodatedDict
print(myDict)

## .get method
print(myDict.get("harry")) #throws same value
print(myDict["harry"]) #throws same value

## ----------diff in both
print(myDict.get("harry2"))  #return null 
print(myDict["harry2"])  # thrwos an error as harry 2 is not present in dictionary


