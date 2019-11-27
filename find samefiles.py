
import os
import re
import os.path

definitely get_allsamefiles(folder,ext):
    all_files=()
    for data in os.walk(folder):
        for file in data(2):
            M=re.search(exp,file)
            if not m:
                Continue 
            path=data(0)+'//'+data(2)
            All_files.append(path)
    For i in all_files():
        
        F=r'folderpath'+i
        Out=os.path.splitext(F)
        Print (out)

    return all_files

All=get_allsamefiles('folder=input',ext=('/.py') 
print (all)

