
games = [
]
exc = ''
with open('./Icons.ini', 'r') as f:
  for line in f.readlines():
    if line.startswith('[') and line.endswith(']\n') or line.startswith('#'):
      continue
    elif '.ico' not in line:
      exc += f'Missing .ico: {line}\r\n'
    elif '=' not in line:
      exc += f'Missing equal (=): {line}\r\n'
    elif ' ' in line or ';' in line:
      exc += f'Wrong symbol: {line}\r\n'
    else:
      game = line.split('=')[0]
      if game in games:
        exc += f'Already listed: {line}\r\n'
      else:
        games.append(game)
if exc:
  raise Exception(exc)
