# This program demonstrates how to write data to a file using Python. It creates a new file called "sample.txt" and writes multiple lines of text into it.
file = open("sample.txt", "w")
# Write data to the file
file.write("Hello, this is my Python and bash assignment.\n")
file.write("Here I am writing data to a file using Python.\n")
file.write("This file was created using the open() and write() functions.\n")
# Close the file after writing
file.close()
# Print a message indicating that the data has been written successfully
print("Data written to sample.txt successfully.")
