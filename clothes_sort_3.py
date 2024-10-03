import argparse

# no errors #
Error = False 

# argparse args #
parser = argparse.ArgumentParser(description= 'Find out where clothes go in your closet')
parser.add_argument('article', nargs= '+', type= str, help= 'input: base type')
parser.add_argument('-r', '--delete', action= 'store_true')
parser.add_argument('-a','--names', action= 'store_true')

args = parser.parse_args()


# clothing base type #        
types = {'p': 'pants', 'd': 'sweats', 's': 'shirt', 'f': 'flanels', 'w': 'winter'}

# clothing subcategories #
black, grey, brown, green, blue, purple= [],[],[],[],[],[]
pink, orange, tan, white, red, long= [],[],[],[],[],[]
flanel, flong = [],[]
big, medium, small = [],[],[]
jeans, light, bulky, shorts, soft, loud, pjs = [],[],[],[],[],[],[]

# dictionary of lists with referances #
lists = {'black': black, 'grey': grey, 'brown': brown, 'green': green, 'blue': blue, 'purple': purple, 
         'pink': pink, 'orange:': orange, 'tan': tan, 'white': white, 'red': red, 'long': long,
         'flanel': flanel, 'flong': flong,
         'big': big, 'medium': medium, 'small': small,                                                             #pass using ':'
         'jeans': jeans, 'light': light, 'bulky': bulky, 'shorts': shorts, 'soft': soft, 'loud': loud, 'pjs': pjs, 'pass:': None}
                


file = open('output.txt', 'r')                               #re-add elements from output.txt to their apropriate lists
cleanclas = 'pass:'        #default to pass:                 #
for line in file.readlines():                                #
    line = line.strip()                                      #
                                                             #
    if ':' in line:                                         ## exclude 'subcat' and 'type' lines
        cleanclas = line.lower()[:-1]                        #
    elif not ':' in cleanclas:                               #
        def dup_prevent(word):                              ## if not article inputted, add to appropriate list 
            if name not in word or cleanclas != argssubcat:  #        
                try: lists[cleanclas].append(word)           #
                except (AttributeError,KeyError): pass       #
                                                             # 
        if len(line.split()) > 1:                           ## send word(s) in line through dup_prevent()
            for word in line.split():                        #
                dup_prevent(word)                            #
        else:                                                #
            word = line                                      #
            dup_prevent(word)                                #
file.close                                                   #


if argssubcat in list(lists):           #
    input_clas = args.article[0]        #
else:                                   #
    print("Error: 2")                   #check subcat is approprtiate
    Error = True                        #
    input_clas = 'pass:'                #
        
name = args.article[1]                            #input add to appropriate list
def input_add(name):                              #
    if not args.delete:                         ### if -r --delete, don't add input
        try: lists[input_clas].append(name)       #
        except AttributeError: pass               #
if args.names:                                  ### if -a --names, add multiple items
    for name in args.article[1:]:                 #
        input_add(name)                           #
else:                                             #
    input_add(name)                               #

Output = ''
for st, nd, cat in [(17,21,' ::Pants::'),(21,24,'\n\n\n ::Sweatpants::'),        #
                    (0,12,'\n\n\n ::Shirts::'),(12,14,'\n\n\n ::Long Sleeve::'), #
                    (14,17,'\n\n\n ::Winter::')]:                                #
    Output += cat                                                                #
    for key, var in (list(lists.items()))[st:nd]:                                #build output doc
        if var != [] and var != None:                                            #
            Output += f'\n    {key.capitalize()}:'                               #
            Output += f'\n{'   '.join(var)}'                                     #



if Error != True:                          #
    with open('output.txt', 'w') as file:  #write output
        file.write(Output)                 #

