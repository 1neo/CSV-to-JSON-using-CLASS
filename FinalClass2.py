#!/usr/bin/env python
# coding: utf-8

# In[50]:


#!/usr/bin/python
import csv, json
import sys

csvFilePath = "C:\\onerec.csv"
jsonFilePath = "fileonerec.json"

class Node(object):
    def __init__(self,label,id,link):
        self.id = id
        self.label = label
        self.link = link
        
    def asdict(self):
        return {'id': self.id, 'label': self.label, 'link': self.link,'Children':[]}
    

def iterate(ob,label,id,link,parent):
    if type(ob) is dict:
        if ob['id']==parent :

            ob['Children'].append(Node(label,id,link).asdict())
          
            return
        else:
            iterate(ob['Children'],label,id,link,parent)
    elif type(ob) is list:
        for a in ob:
            iterate(a,label,id,link,parent)

try:
    header=[]    
    data=[]    
    root={}

    nodelist=[]
    k=0
    x=-1

    with open (csvFilePath,'r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        header=csvReader.fieldnames

    
    with open (csvFilePath,'r') as csvFile:
        csvReader = csv.reader(csvFile)
        for csvRow in csvReader:
            if k==0 :
                k=1
                continue
            for i in range(1,len(header),3):
                if not (csvRow[i]):
                    continue
                if i==1 and (csvRow[i+1] not in nodelist) :
                    data.append(Node(csvRow[i],csvRow[i+1],csvRow[i+2]).asdict())
                    nodelist.append(csvRow[i+1])
                    base=csvRow[i-1]
                    x=x+1
                parent= i+1 - 3
                if csvRow[i+1] not in nodelist:
                    iterate(data[x],csvRow[i],csvRow[i+1],csvRow[i+2],csvRow[parent])
                    nodelist.append(csvRow[i+1])

    root[base]= data   
    with open(jsonFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(root, indent = 4))
        
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Value Error.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# In[ ]:




