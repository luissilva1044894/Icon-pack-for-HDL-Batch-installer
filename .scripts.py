
import os
from os.path import (
  abspath,
  dirname,
  join,
  isfile,
)
import re

GAMES = [
]
EXC = ''
DEV_ID_RE = re.compile(r'^[a-zA-Z]{2}[0-9]{3}\-?[a-zA-Z]{1}[0-9]{1}$')
TITLE_ID_RE = re.compile(r'^(?P<type>[a-zA-Z]{4})\_?(?P<id>[0-9]{3}\.?[0-9]{2})(?P<release>[a-zA-Z]{1})*$')
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
      #Ignore weird id
      if 'ARP2_012.01' not in game and TITLE_ID_RE.match(game) is None and DEV_ID_RE.match(game) is None:
        EXC += f'Wrong Title ID: {line}\r\n'
      elif game in GAMES:
        EXC += f'Already listed: {line}\r\n'
      else:
        ico_path = join(ICONS_FOLDER, ico.replace('\n', ''))
        if not isfile(ico_path) or not os.access(ico_path, os.R_OK):
          EXC += f'.ico not found: {ico}\r\n'
        GAMES.append(game)
if EXC:
  raise Exception(EXC)
