import os
from beautifultable import BeautifulTable
ret = os.popen('netsh wlan show profiles name=* key=clear | findstr "name"')
data = ret.read()
lines = data.splitlines()



SSID_names = []


for i in lines:
    SSID_names.append(i[i.find(":")+3 :-1])


data2 = ''
for i in range(len(lines)):
    ret_pass = os.popen(f'netsh wlan show profiles name="{SSID_names[i]}" key=clear | findstr "Key Content"')
    
    check = ret_pass.read()
    if len(check) == 0:
        data2 += '\n'
    if len(check) == 31:
        data2+= '\n'
    else:
        data2 += check
    
lines2 = data2.splitlines()

#print(data2)
#print(lines2)

SSID_pass = []


for i in lines2:
    SSID_pass.append(i[i.find(":")+2 ::])


table = BeautifulTable()
table.columns.header = ["SSID Username", "SSID Password"]

for i in range(len(lines)):
    table.rows.append([SSID_names[i],SSID_pass[i]])
print(table)