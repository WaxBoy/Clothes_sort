#ignore
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x = ['a'],['b'],['c'],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],['s'],['t'],['u'],['v'],['w'],['x']
#ignore
lists = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'l': l, 'm': m, 'n': n, 'o': o, 'p': p, 'q': q, 'r': r, 's': s, 't': t, 'u': u, 'v': v, 'w': w, 'x': x}
#ignore


#copy & replace
Output = ''
for st, nd, cat in [(17,21,' ::Pants::'),(21,23,'\n\n\n ::Sweatpants::'),(0,12,'\n\n\n ::Shirts::'),(12,14,'\n\n\n ::Long Sleeve::'),(14,17,'\n\n\n ::Winter::')]:
    Output += cat
    for key, var in (list(lists.items()))[st:nd]:
        if var != [] and var != None:     
            Output += f'\n    {key.capitalize()}:'
            Output += f'\n{'   '.join(var)}'
print (Output)
#copy & replace