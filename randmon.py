from extras.pokemontools.pokemon_constants import pokemon_constants
from extras.pokemontools.move_constants import moves
import re
import random
import os

def no_newline_open(path):
    return [x.replace('\n', '') for x in open(path).readlines()]

# load files
trainer_file = no_newline_open('./trainers/trainers.asm')
new_trainer_file = []

johto_grass = no_newline_open('./data/wild/johto_grass.asm')
new_johto_grass = []

kanto_grass = no_newline_open('./data/wild/kanto_grass.asm')
new_kanto_grass = []

# load mon/move constants
mons = pokemon_constants.values()
moves = moves.values()

# trainer file regexp
mon_regex = re.compile('\tdb (\d\d?), (.*)(, .*)?')
move_regex = re.compile('\t\tdb (.*)')
inside_mon = False

print 'Randomising trainers...'
for line in trainer_file:
    match = mon_regex.match(line)
    if match:
        # print match.groups()
        inside_mon = True
        rmon = random.choice(mons)
        print 'Replacing %s with %s...' % (match.groups()[1], rmon)
        new_trainer_file.append('\tdb %s, %s' % (match.groups()[0], rmon))
        # print 'Replacing %s with %s.' % (match.groups()[1], rmon)
    elif line == '':
        inside_mon = False
        new_trainer_file.append('')
    elif inside_mon:
        match2 = move_regex.match(line)
        if match2:
            rmov = random.choice(moves)
            print ' - Replacing %s with %s...' % (match2.groups()[0], rmov)
            new_trainer_file.append('\t\tdb %s' % rmov)
            # print ' - Replacing %s with %s.' % (match2.groups()[0], rmov)
            # print match2.groups()
    else:
        new_trainer_file.append(line)

wmon_regex = re.compile('\tdb (\d\d?), (.*)')

print 'Randomising Johto wild data...'
for line in johto_grass:
    match3 = wmon_regex.match(line)
    if match3:
        rmon = random.choice(mons)
        print 'Replacing %s with %s...' % (match3.groups()[1], rmon)
        new_johto_grass.append('\tdb %s, %s' % (match3.groups()[0], rmon))
    else:
        new_johto_grass.append(line)

print 'Randomising Kanto wild data...'
for line in kanto_grass:
    match3 = wmon_regex.match(line)
    if match3:
        rmon = random.choice(mons)
        print 'Replacing %s with %s...' % (match3.groups()[1], rmon)
        new_kanto_grass.append('\tdb %s, %s' % (match3.groups()[0], rmon))
    else:
        new_kanto_grass.append(line)
    
os.rename('./trainers/trainers.asm', './trainers/trainers_old.asm')
f1 = open('./trainers/trainers.asm', 'wb+')
f1.write('\n'.join(new_trainer_file))
f1.close()
os.rename('./data/wild/johto_grass.asm', './data/wild/johto_grass_old.asm')
f2 = open('./data/wild/johto_grass.asm', 'wb+')
f2.write('\n'.join(new_johto_grass))
f2.close()
os.rename('./data/wild/kanto_grass.asm', './data/wild/kanto_grass_old.asm')
f3 = open('./data/wild/kanto_grass.asm', 'wb+')
f3.write('\n'.join(new_kanto_grass))
f3.close()
# print '\n\n\n'
# print '\n'.join(new_trainer_file)