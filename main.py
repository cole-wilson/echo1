def search(word):
  length = len(word)
  t= False
  for x in range(len(insult)):
    if insult[x:x+length] == word:
      return True
      t = True
  if t != True:
    return False

import random
import time

y = ''
name = ''
print('Hello, I am Echo. Insult me if you dare!')
while True:
  insult = input('>>>')
  insult = insult.lower()
  if search('hi') or search('hello'):
    if name != '':
      print('Hello ' + name + '!')
    else:
      print('Hello, what is your name?')
      name = input('Name:')
      if name == 'thanos' or name == 'Thanos':
        print('Don\'t make me do it...')
        time.sleep(1)
        print('*snap*')
        
      else:
        print('Hello ' + name + '!')
  elif insult[0:3] == 'you':
    if search('bum') or search('heck') or search('damn') or search('frick'):
      print('NO SWEARING ON MY AGNOSTIC WEB SERVER!!!!!!!!!')
    elif search('idiot') or search('dumb') or search('not   smart') or search('stupid'):
      print('Ha, you think I\'m dumb? Try to solve this:')
      a = random.randint(-1000,1000)
      b = random.randint(-1000,1000)
      print(str(a) + ' times ' + str(b))
      time.sleep(2)
      print('That was easy for me, the answer is: ' + str(a*b))
    else:
      choice = random.randint(0,1)
      if choice == 0:
        print('no u')
      else:
        print('that\'s rude')
  elif search('reverse card'):
      print('doesn\'t work')
  elif search('i '):
    print('I think we all know how true that is ' + name + '.')
  else:
    choice = random.randint(0,1)
    if choice == 0:
      print('no u')
    else:
      print('that\'s rude')