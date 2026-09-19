# This program demonstrates how to read data from a file using Python. It opens an existing file called "sample.txt" and reads its contents, displaying them on the console.
file = open("sample.txt", "r")
# Read data from the file
content = file.read()
# Print the contents of the file
print("File contents:")
print(content)
# Close the file after reading
file.close()
