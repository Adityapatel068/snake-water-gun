print(f'welcome to snake water gun made by aditya'.center(50,'_'))
import time
p = '''snake = s
gun   = g
water = w'''
print(p)
time.sleep(2)
i = input('choose your sign:- ')
import random
ai = random.choice(['s', 'g', 'w'])
time.sleep(2)
print(f'Bot choose {ai}')
if "s" in i and "s" in ai:
  time.sleep(3.5)
  print('draw')
elif "s" in i and "g" in ai:
  time.sleep(3.5)
  print('you lose')
if "s" in i and "w" in ai:
  time.sleep(3.5)
  print('you win')
if "g" in i and "s" in ai:
  time.sleep(3.5)
  print('you win')
elif "g" in i and "g" in ai:
  time.sleep(3.5)
  print('draw')
if "g" in i and "w" in ai:
  time.sleep(3.5)
  print('you lose')
if "w" in i and "s" in ai:
  time.sleep(3.5)
  print('you lose')
elif "w" in i and "g" in ai:
  time.sleep(3.5)
  print('you win')
if "w" in i and "w" in ai:
  time.sleep(3.5)
  print('you draw')