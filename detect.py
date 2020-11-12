from datetime import date, datetime

today = date.today()
today = today.strftime("%b %d")
whitelist = []
blacklist = []

with open('whitelist.txt','r') as w, open('auth_filter.log','r') as f:
    
    for wlist in w:
        whitelist.append(wlist.strip())
    
    for line in f:
        date = datetime.strptime(line[:6], "%b %d").date()
        date = date.strftime("%b %d")
        if date == today:
            x = line.find(' from ') 
            if x != -1:
                y = line.find(' port') 

                if line[x+6:y] not in whitelist:
                    blacklist.append(line[x+6:y]) 

blacklist = list(set(blacklist)) 

print ('whitelist :', whitelist)
print ('blacklist :', blacklist)

#print(date==today)