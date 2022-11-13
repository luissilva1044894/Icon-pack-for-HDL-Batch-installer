
games = [
]
exc = ''
with open('Icons.ini', 'r') as f:
  for l in f.readlines():
    if '[ICONS]' in l or '#' in l:
      continue
    elif '.ico' not in l or '=' not in l or ' ' in l:
      exc += f'Error: {l}\r\n'
    else:
      x = l.split('=')[0]
      if x in games:
        exc += f'Duplicated: {x}\r\n'
      else:
        games.append(x)
if exc:
  raise Exception(exc)
print('OK!')
