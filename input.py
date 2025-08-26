with open("input.txt", "w") as file:
        file.write("This is the first time.\n")
        file.write("Python is fun to learn and interactive.\n")
        file.write("We are learning file handling.\n")
        file.write("File handling is very useful.\n")
        file.write("Let's complete this project!\n")
try:

    with open("input.txt", "r") as file:
        content = file.read()
        word_count = len(content.split())
        uppercase_content = content.upper()

    with open("output.txt", "w") as file:
        file.write("PROCESSED TEXT:\n")
        file.write(uppercase_content)
        file.write("\n")
        file.write(f"WORD COUNT: {word_count}\n")

    print("Success! The processed text has been written to output.txt.")

except FileNotFoundError:
    print('Error: File not found.')
except Exception as e:
    print('Error:', e)