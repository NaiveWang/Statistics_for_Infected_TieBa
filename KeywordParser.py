import codecs

def gen(n,m,phase,s):
    if n==m:
        print(s)
        return
    for temp in phase[n]:
        s0 = s+temp
        gen(n+1,m,phase,s0)
    return



f = codecs.open('moha.psr','r','utf-8')
text = f.read()

line = text.split('\n')
parse = []
for a in line:#Context free,spilt the line
    t = a.split('+')
    phase = []
    for b in t:
        words = b.split('#')
        phase.append(words)
    parse.append(phase)
#parse ended
print(parse)
s=''
print(len(parse)-1)
gen(0,3,parse[1],s)