course = "Python for beginners"
# string to upper case, doesn't change the original object var, returns a new string object in memory
print(course.upper())
# find occurences returns index (returns 7)
print(course.find("for"))
# find occurences returns index (returns -1) as it doesn't exist
print(course.find("Y"))
# replacing string
print(course.replace("for", "4"))
# returns boolean values if it exists (returns true)
print("Pyhton" in course)