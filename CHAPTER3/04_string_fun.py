from turtle import st


story = "once upon a time there was a youtuber named Harry who uploaded python course with notes"

# String functions

# 1. len function
print(len(story))

# 2. endswith function
print(story.endswith("notes"))
print(story.endswith("s"))
print(story.endswith("dfnd"))

# 3. count function
print(story.count("o"))
print(story.count("a"))
print(story.count("y"))

# 4. capitalize
print(story.capitalize())

# 5. find function
print(story.find("once")) #0
print(story.find("hfsd")) #-1

# 6. replace
print(story.replace("Harry", "Manish"))

