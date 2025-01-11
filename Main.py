
# Change this with your own file
file_path = "c:\\Users\\asshl\\Downloads\\CorrectAnswers.txt"

def load_file(file_path = "c:\\Users\\asshl\\Downloads\\CorrectAnswers.txt"):

    with open(file_path, "r", encoding='utf-8') as file:
        content = file.read()
    return content

loaded_file = load_file(file_path)

# Counter by number of words
def by_words(file):

    total_words = 0
    words = file.split()

    for word in words:
        total_words = total_words + 1
    print(f"Total number of words: {total_words}")

# Count by number of characters
def by_characters(file):

    characters = str(file)
    print(f"Total number of characters: {len(characters)}")

# Count by number of lines  
def by_lines(file):

    with open(file_path, "r") as file:
        content = file.readlines()
    total_lines = content.count(content)
    
    for line in content:
        total_lines += 1
    print(f"Total number of lines: {total_lines}")

by_characters(loaded_file)
by_lines(loaded_file)
by_words(loaded_file)