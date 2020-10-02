from nltk.util import ngrams
import re
from random import choice


def load_data():
    with open('church_list.txt') as f:
        all_church = f.readlines()
        all_church = [x.strip().replace('.', '') for x in all_church]
    return all_church

all_church = load_data()

def get_both_upper(bihram):
  filtered = []
  for x in bihram:
    try:
      if x[0][0].isupper() and x[1][0].isupper():
        filtered.append(x)
    except IndexError:
      pass
  return list(set([x for x in filtered if not (',' in x[0] or ',' in x[1])]))


def get_both_lower(bihram):
  filtered = []
  for x in bihram:
    try:
      if x[0][0].islower() and x[1][0].islower():
        filtered.append(x)
    except IndexError:
      pass
  return list(set([x for x in filtered if not (',' in x[0] or ',' in x[1])]))


def get_upper_and_lower(bihram):
  filtered = []
  for x in bihram:
    try:
      if x[0][0].isupper() and x[1][0].islower():
        filtered.append(x)
    except IndexError:
      pass
  return list(set([x for x in filtered if not (',' in x[0] or ',' in x[1])]))


def fem_suffix(names_set):
  f = [x for x in names_set if  x[0].endswith(('ы', 'и', 'ой'))]
  f = [x for x in f if x[0][:-2] != x[1][:-2] and x[0] not in ('Ильи', 'Илии')]
  return f


def get_hram(set_tuples:set) -> list:
  return [x for x in set_tuples if 'храм' in x]


def filter_names(upper_set:set) -> list:
  return [x for x in upper_set if x[0][-2:] != x[1][-2:]]


def iy_adj(bihram:list)-> list:
  flatten = [a for tup in bihram for a in tup]
  loc = set(["".join([ c if c.isalnum() else " " for c in  x]).strip() for x in flatten if x.endswith('ий')]) #дофильтровать вручную
  return list(loc)


def get_random_string(name:tuple, adj:str, hram:tuple):
  name = choice(name)
  adj =  choice(adj)
  hram = choice(hram)
  return f'{name[0]} {name[1]} {hram[0]} {hram[1]}'


def get_by_category(all_church:list, category:str)->list:
  return [x for x in all_church if category in x]

def get_hrams(all_church):
  return [x for x in all_church if 'храм' in x]

def get_churchs(all_church):
   return [x for x in all_church if 'церковь' in x]


def get_sobors(all_church):
  return [x for x in all_church if 'собор' in x]


def get_chas(all_church):
  return [x for x in all_church if 'часовня' in x]


def get_bihram(items):
  return [list(ngrams(x.replace('.', '').split(' '), 2))[0] for x in items]




def generator():
  items = get_by_category(all_church, 'церковь')
  bihram = get_bihram(items)
  get_hram = get_upper_and_lower(bihram)
  both_upper = get_both_upper(bihram)
  filtered_names = filter_names(both_upper)
  adj = iy_adj(bihram)
  return get_random_string(filtered_names, adj, get_hram)


def random_from_list():
  return choice(all_church)


if __name__ == '__main__':
    random_from_list()

