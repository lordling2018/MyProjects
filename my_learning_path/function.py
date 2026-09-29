# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green_peppers', 'extra_cheese')

# def make_pizza(*toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a pizza with the following tippings: ")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green_peppers', 'extra_cheese')

# def build_profile(first, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)
import sys
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')