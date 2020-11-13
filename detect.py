from datetime import date, datetime
import json

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
                    #print(blacklist)

                    json_string = json.dumps(blacklist)
                    with open("./blacklist.txt", "w") as file:
                        file.write(json_string)

#blacklist = list(set(blacklist))

#json_string = json.dumps(blacklist)
#with open("./blacklist.txt", "w") as file:
#    file.write(json_string)
    
#print(json_string)
#print ('whitelist :', whitelist)
#print ('blacklist :', blacklist)

#print(date==today)