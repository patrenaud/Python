# Writing to a txt file

print("Creating a text file with the write() method")

textFile = open("writeIt.txt", "w")
textFile.write("Line 1\n")
textFile.write("This is Line 2 \n")
textFile.write("That makes it Line 3")
textFile.close()


print("Reading a text file with the write() method")
textFile = open("writeIt.txt", "r")
print(textFile.read())
textFile.close()

print("\nCreating a text file with the writelines() method")
textFile = open("writeIt.txt", "w")
lines = ["1\n", "2\n", "3\n"]
textFile.writelines(lines)
textFile.close()

textFile = open("writeIt.txt", "r")
print(textFile.read())
textFile.close()

input("\n\nPress any key to exit")
