
import os
from os.path import (
  abspath,
  dirname,
  join,
  isfile,
)

GAMES = [
]
EXC = ''
ICONS_FOLDER = join(abspath(dirname(__file__)), 'ICNS')
with open('./Icons.ini', 'r') as f:
  for line in f.readlines():
    if line.startswith('[') and line.endswith(']\n') or line.startswith('#'):
      continue
    elif '.ico' not in line:
      EXC += f'Missing .ico: {line}\r\n'
    elif '=' not in line:
      EXC += f'Missing equal (=): {line}\r\n'
    elif ' ' in line or ';' in line:
      EXC += f'Wrong symbol: {line}\r\n'
    else:
      game, ico = line.split('=', 1)
      if game in GAMES:
        EXC += f'Already listed: {line}\r\n'
      else:
        ico_path = join(ICONS_FOLDER, ico.replace('\n', ''))
        if not isfile(ico_path) or not os.access(ico_path, os.R_OK):
          EXC += f'.ico not found: {ico}\r\n'
        GAMES.append(game)
if EXC:
  raise Exception(EXC)
