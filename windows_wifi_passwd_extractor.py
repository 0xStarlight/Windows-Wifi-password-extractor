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
    ret_pass = os.popen(f'netsh wlan show profiles name={SSID_names[i]} key=clear | findstr "Key Content"')
    data2 += ret_pass.read()
lines2 = data2.splitlines()

SSID_pass = []

for i in lines2:
    SSID_pass.append(i[i.find(":")+2 :-1])

table = BeautifulTable()
table.columns.header = ["SSID Username", "SSID Password"]

for i in range(len(lines)):
    table.rows.append([SSID_names[i],SSID_pass[i]])
print(table)
