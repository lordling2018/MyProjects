bicycles = ['trek','cannondale','redline','specialized']
bicycles[0] = 'comm-trek'
bicycles.append("last-one")
bicycles.insert(0,'first-one')
print(bicycles)
del bicycles[0]
print(bicycles)
print(bicycles[bicycles.index('cannondale')])
pop1 = bicycles.pop()
print(f"the last bicycle i owned was a {pop1.title()}")
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
print(sorted(bicycles,reverse=True))
print(bicycles)
bicycles.reverse()
print(bicycles)
print(len(bicycles))
for bicycle in bicycles:
    print(bicycle)
for bicycle in bicycles:
    print(f"{bicycle.title()}, that was a beautiful bicycle")
for value in range(1,11,2):
    print(value)
squares = []
for value in range(1, 11):
#    square = value ** 2
    squares.append(value ** 2)

print(squares)    
print(min(squares))
print(max(squares))
print(sum(squares))
squares = [value**2 for value in range(1,11)]
print(squares)
print(bicycles[-2:])
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f"my favorite foods are: {my_foods} !")
print(f"my favorite foods are: {friend_foods} !")
current_user1 = ['Jason', 'Peter', 'LORDLING', 'mouse', 'Victor']
new_users = ['LORDLING', 'daniel', 'Jupter', 'sala', 'Mouse']
current_user2 = [user.lower() for user in current_user1]
print(current_user2)
for new_user in new_users:
    if new_user.lower() in current_user2:
        print('!!!same user name, please input another name!')
    else:
        print('good user name, please conintue go ahead!')
numbers = list(range(1, 10))
print(numbers)
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    elif number == 4:
        print('4th')
    elif number == 5:
        print('5th')
    elif number == 6:
        print('6th')
    elif number == 7:
        print('7th')
    elif number == 8:
        print('8th')    
    elif number == 9:
        print('9th')
