import os

os.remove('./trainers/trainers.asm')
os.remove('./data/wild/johto_grass.asm')
os.remove('./data/wild/kanto_grass.asm')

os.rename('./trainers/trainers_old.asm', './trainers/trainers.asm')
os.rename('./data/wild/johto_grass_old.asm', './data/wild/johto_grass.asm')
os.rename('./data/wild/kanto_grass_old.asm', './data/wild/kanto_grass.asm')