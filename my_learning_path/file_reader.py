from pathlib import Path

path = Path('day01/pi_million_digits.txt')
contents = path.read_text()
# contents = contents.rstrip()
# print(contents)
lines = contents.splitlines()
# for line in lines:
#     print(line)
pi_string = ' '
for line in lines:
    pi_string += line.lstrip() 
pi_string = pi_string.lstrip()
# print(f"{pi_string[:52]}...")
# print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if (birthday in pi_string):
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appears in the first million digits of pi!")


