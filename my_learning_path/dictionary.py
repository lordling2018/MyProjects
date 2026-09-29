# alien_0 = {'color':'green', 'points':5}
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# alien_0['color'] = 'yellow'
# alien_0['x_position'] = 100
# print(alien_0)
# del alien_0['points']
# print(alien_0)
# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',    
#     }
# for name, language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")
# for name in favorite_language.keys():
#     print(name.title())
# friends = ['phil', 'sarah']
# for name in favorite_language.keys():
#     print(f"Hi, {name.title()}")
#     if name in friends:
#         language = favorite_language[name].title()
#         print(f"\t{name.title()}, I see you love {language}")
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)   
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print("......") 
# print(f"Total number of aliens: {len(aliens)}")   
# favorite_language = {
#     'jen': ['phthon', 'rust'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['phtyon', 'hashell'],
#     }
# for name, languages in favorite_language.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         if len(languages) == 1:
#             print(f"\tonly one language: {language.title()}")
#         else:
#             print(f"\t{language.title()}")
users = {
    'aeinsten': {
        'first': 'albert',
        'last': 'einsten',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
# for username, user_info in users.items():
#     print(f"\nusername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")
sandswich_orders = ['sandswich_1', 'pastrami', 'sandswich_2', 'pastrami','sandswich_3', 'pastrami',]
finished_sandswiches = []
# while sandswich_orders:
#     current_sandswich = sandswich_orders.pop()
#     print(f"I made your tuna sandswich: {current_sandswich.title()}")
#     finished_sandswiches.append(current_sandswich)
# for finished_sandswich in finished_sandswiches:
#     print(finished_sandswich.title())
print(sandswich_orders)
while 'pastrami' in sandswich_orders:
    sandswich_orders.remove('pastrami')
print(sandswich_orders)    