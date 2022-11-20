
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

def ignored_symbols(entry):
  return entry.startswith('[') and entry.endswith(']\n') or entry.startswith('#')
def ignored_ids(game_id):
  return 'ARP2_012.01' in game_id or \
         'KOEI_SP0.02' in game_id
def is_valid_game_id(game_id):
  return ignored_ids(game_id) or TITLE_ID_RE.match(game_id) is not None or DEV_ID_RE.match(game_id) is not None
def has_icon_file(path):
  if ICONS_FOLDER not in path:
    path = join(ICONS_FOLDER, path)
  return isfile(path) and os.access(path, os.R_OK)
def check_entries(entry):
  if '.ico' not in entry:
    return f'Missing .ico: {entry}\r\n'
  if '=' not in entry:
    return f'Missing equal (=): {entry}\r\n'
  if ' ' in entry or ';' in entry or '__' in entry:
    return f'Wrong symbol: {entry}\r\n'

with open('./Icons.ini', 'r') as f:
  for line in f.readlines():
    if ignored_symbols(line):
      continue
    ret = check_entries(line)
    if ret:
      EXC += ret
    else:
      game, ico = line.split('=', 1)
      if not is_valid_game_id(game):
        EXC += f'Wrong Title ID: {line}\r\n'
      elif game in GAMES:
        EXC += f'Already listed: {line}\r\n'
      else:
        if not has_icon_file(ico.replace('\n', '')):
          EXC += f'.ico not found: {ico}\r\n'
        GAMES.append(game)
if EXC:
  raise Exception(EXC)
print('Everything is Ok!')
