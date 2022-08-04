import os
import time

spisok = []

for adress, dirs, files in os.walk('‪D:\\Parser'):
    for file in files:
        full = os.path.join(adress,file)
        spisok.append(full)

print(spisok)
                
