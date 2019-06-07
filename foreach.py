
names = ['yossi', 'dana','orli', 'yosef']

print(names)
# for loop
# foreach name in named do
#for name in reversed(names):

for name in names:
    #print(f'{name} is type {type(name)}')
    if name == 'orli':
        break # exit the loop
    print(f'{name}')
    if name == 'dana':
        print('this is dana')


