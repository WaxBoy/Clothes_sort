import argparse

Error = False

parser = argparse.ArgumentParser(description= 'Find out where clothes go in your closet')
parser.add_argument('article', nargs= '+', type= str, help= 'print; p,f,s,l,w')
parser.add_argument('-r', '--delete', action= 'store_true')
parser.add_argument('-a','--names', action= 'store_true')
#parser.add_argument('-l', '--lists', action= 'store_true', help= 'allow lists')

args = parser.parse_args()

argssubcat = args.article[0]
name = args.article[1]


        #article of clothing
types = {'p': 'pants', 'd': 'sweats', 's': 'shirts', 'f': 'flanels', 'w': 'winter'}

black, grey, brown, green, blue, purple= [],[],[],[],[],[]
pink, orange, tan, white, red, long= [],[],[],[],[],[]
flanel, flong = [],[]
big, medium, small = [],[],[]
jeans, light, bulky, shorts, soft, loud, pjs = [],[],[],[],[],[],[]

lists = {'black': black, 'grey': grey, 'brown': brown, 'green': green, 'blue': blue, 'purple': purple, 
         'pink': pink, 'orange:': orange, 'tan': tan, 'white': white, 'red': red, 'long': long,
         'flanel': flanel, 'flong': flong,
         'big': big, 'medium': medium, 'small': small,
         'jeans': jeans, 'light': light, 'bulky': bulky, 'shorts': shorts, 'soft': soft, 'loud': loud, 'pjs': pjs, 'pass:': None}



if argssubcat in list(lists):
    input_clas = argssubcat   #if a correct subcat, set clas
else:
    print("Error: 2")       
    Error = True
    input_clas = 'pass:'   




file = open('output.txt', 'r')  
cleanclas = 'pass:'
for line in file.readlines():
    line = line.strip()
    if ':' in line: 
        cleanclas = line.lower()[:-1]
    elif not ':' in cleanclas:   
        def dup_prevent(word):
            if name in word and cleanclas == argssubcat:        
                pass
            else: 
                try: lists[cleanclas].append(word) 
                except (AttributeError,KeyError): pass
        if len(line.split()) > 1:
            for word in line.split():
                dup_prevent(word)
        else:
            word = line
            dup_prevent(word)
file.close

def input_add(name):
    if not args.delete:
        try: lists[input_clas].append(name)
        except AttributeError: pass
#-a --names  
if args.names:  
    for name in args.article[1:]:
        input_add(name)
else:
    input_add(name)   

Output = ''
for st, nd, cat in [(17,21,' ::Pants::'),(21,24,'\n\n\n ::Sweatpants::'),
                    (0,12,'\n\n\n ::Shirts::'),(12,14,'\n\n\n ::Flanels::'),
                    (14,17,'\n\n\n ::Winter::')]:
    Output += cat
    for key, var in (list(lists.items()))[st:nd]:
        if var != [] and var != None:     
            Output += f'\n    {key.capitalize()}:'
            Output += f'\n{'   '.join(var)}'



if Error != True:
    with open('output.txt', 'w') as file:
        file.write(Output)

