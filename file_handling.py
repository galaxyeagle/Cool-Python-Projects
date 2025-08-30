# 1. Creating a new file and adding content

with open('file.txt', 'w') as f:
    f.write("""In the world of python programming, creativity knows no bounds.
Many developers love python for its simplicity and powerful libraries.
Learning python opens doors to data science, web development, and automation.
The community around python is vibrant and always ready to help beginners.
Python syntax is designed to be readable and easy to understand.
Coding is an art that brings ideas to life.
""")




# 2. Reading and printing the file contents line by line

with open('file.txt', 'r') as f:
    for line_number, line in enumerate(f, start=1):
        print(f"Line {line_number}: {line.strip()}")

# Printing the total word count in this file

    f.seek(0)
    content = f.read()
    word_count = len(content.split())
    print(f"\nTotal word count: {word_count}")

# Copy contents in a new file

    f.seek(0)
    with open('copy_file.txt', 'w') as copy_f:
      copy_f.write(f.read())
    print("\nFile copied successfully!")




# 3. Printing lines containing "python"

print("Lines containing the word \"Python\" are :")
with open('file.txt', 'r') as f:
  for line_number, line in enumerate(f, start=1):
    if 'python' in line.lower():
      print(f"{line_number}: {line.strip()}")





# 4. Create a new file and enter students' names from user input

with open('students.txt','w') as s:
  while True:
    name = input("Enter the student's name(Or enter END to finish)")
    if name.lower() == 'end'':
      break
    s.write(name + '\n')

print("Student names saved to students.txt :")
with open('students.txt', 'r') as s:
  print(s.read())
