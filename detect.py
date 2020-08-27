whitelist = []
blacklist = []

with open('whitelist.txt','r') as w, open('auth_filter.log','r') as f:
    
    for wlist in w:
        whitelist.append(wlist.strip())
    
    for line in f:
        x = line.find(' from ') 
        if x != -1:
            y = line.find(' port') 

            if line[x+6:y] not in whitelist:
                blacklist.append(line[x+6:y]) 

blacklist = list(set(blacklist)) 

print ('whitelist :', whitelist)
print ('blacklist :', blacklist)