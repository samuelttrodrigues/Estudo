# A) Tabuada do 1 ao 10 utilizando 2 while
# B) Tabuada do 1 ao 10 utilizando 2 for
# C) Tabuada do 1 ao 10 utilizando 1 while e 1 for

#! A)

tabuada = 1

while (tabuada <= 10):
    print(f'\nTábuada do {tabuada}:\n')    
    multi = 0
    while (multi <= 10):
        print(f'{tabuada} x {multi} = {tabuada * multi}')
        multi += 1
    tabuada += 1

#! B) dois for

for i in range (1,11,1):
    print(f'\nTábuada do {i}\n')
    for e in range (0,11,1):
        print(f'{i} x {e} = {i * e}')
        e += 1
    i += 1

#! C) um while e um for

tab = 1

while (tab <= 10):
    print(f'\nTábuada do {tab}\n')
    for z in range (0,11,1):
        print (f'{tab} x {z} = {tab * z}')
        tab +=1