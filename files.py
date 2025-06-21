 #Read a Text File
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:\n", content)

#2. Write Text to .txt File (simulating InputStream)
def write_text_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)


#Read a File Stream
def read_file_stream(file_path):
    with open(file_path, 'rb') as file:
        while chunk := file.read(64):  # Read in 64-byte chunks
            print(chunk.decode(), end="")
#Read a File Stream with Random Access Support
def random_access_read(file_path):
    with open(file_path, 'rb') as file:
        file.seek(10)  # Move 10 bytes from the start
        data = file.read(20)  # Read next 20 bytes
        print("Randomly accessed data:", data.decode())

#Read File from Specific Index Using seek()
def read_from_index(file_path, index):
    with open(file_path, 'r') as file:
        file.seek(index)
        print("From index", index, ":", file.read())

# Example
read_from_index("example.txt", 5)



