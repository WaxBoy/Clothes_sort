import argparse

Error = False

parser = argparse.ArgumentParser(description= 'Find out where clothes go in your closet')
parser.add_argument('article', nargs= '+', type= str, help= 'print; p,f,s,l,w')
parser.add_argument('-r', '--delete', action= 'store_true')
parser.add_argument('-a','--names', action= 'store_true')
#parser.add_argument('-l', '--lists', action= 'store_true', help= 'allow lists')

args = parser.parse_args()

argssubcat = args.article[0]
argsname = args.article[1]


        #article of clothing
types = {'p': 'pants', 'f': 'sweats', 's': 'shirt', 'l': 'long', 'w': 'winter'}

black, grey, brown, green, blue, purple= [],[],[],[],[],[]
pink, orange, tan, white, red, flanel= [],[],[],[],[],[]
sleeve, lfanel = [],[]
big, medium, small = [],[],[]
jeans, light, bulky, shorts, soft, loud = [],[],[],[],[],[]

lists = {'black': black, 'grey': grey, 'brown': brown, 'green': green, 'blue': blue, 'purple': purple, 
         'pink': pink, 'orange:': orange, 'tan': tan, 'white': white, 'red': red, 'flanel': flanel,
         'sleeve': sleeve, 'lfanel': lfanel,
         'big': big, 'medium': medium, 'small': small,
         'jeans': jeans, 'light': light, 'bulky': bulky, 'shorts': shorts, 'soft': soft, 'loud': loud, 'pass:': None}



if argssubcat in list(lists):
    clas = argssubcat   #if a correct subcat, set clas
else:
    print("Error: 2")       
    Error = True
    clas = 'pass:'   

name = argsname

def list_builder(name):
        if not args.delete:
            try: lists[clas].append(name)
            except AttributeError: pass

file = open('output.txt', 'r')  

cleanclas = 'pass:'
for line in file.readlines():
    line = line.strip()
    if ':' in line: 
        cleanclas = line.lower()[:-1]
    else:   
        if line != name or cleanclas != argssubcat and not ':' in cleanclas:
            try: lists[cleanclas].append(line)    #subcat = Bulky: --> bulky
            except (AttributeError,KeyError): pass

if args.names:
    for name in args.article[1:]:
        list_builder(name)
else:
    list_builder(name)   

Output = '::Pants::'
for key, var in (list(lists.items()))[17:21]:
    if var != [] and var != None:     
        Output += f'\n    {key.capitalize()}:'
        Output += f'\n{'   '.join(var)}'
        print(var)

Output += '\n::Sweatpants::'
for key, var in (list(lists.items()))[21:23]:
    if var != [] and var != None:       
        Output += f'\n   {key.capitalize()}:'
        Output += f'\n{'   '.join(var)}'

Output += '\n::Shirts::'
for key, var in (list(lists.items()))[0:12]:
    if var != [] and var != None:       
        Output += f'\n   {key.capitalize()}:'
        Output += f'\n{'   '.join(var)}'

Output += '\n::Long Sleeve::'
for key, var in (list(lists.items()))[12:14]: 
    if var != [] and var != None:       #var is list of names in each sub category
        Output += f'\n   {key.capitalize()}:'
        Output += f'\n{'   '.join(var)}'

Output += '\n::Winter::'
for key, var in (list(lists.items()))[14:17]:
    if var != [] and var != None:      
        Output += f'\n   {key.capitalize()}:'
        Output += f'\n{'   '.join(var)}'



if Error != True:
    with open('output.txt', 'w') as file:
        file.write(Output)


# read lines of file if line has no semicolon, becomes subcategory.