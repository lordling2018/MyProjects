from pathlib import Path

# path = Path('day01/programming.txt')
# contents = "I love programming!\n"
# contents += "I love creating new games!\n"
# contents += "I also love working with data!\n"
# path.write_text(contents)

prompt = "\nTell me your name, I will store your name in the name_list.txt file!"
prompt += "\nOr Enter 'quit' to end the program!"

message = input(prompt)
path = Path('day01/name_list.txt')
while message.lower() != 'quit':
    old_message = path.read_text()
    message = old_message + message + "\n"
    path.write_text(message)
    message = input(prompt)
    