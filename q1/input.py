import random
import csv

def csvfile(file_name, lst):
    
    fp = open(file_name, 'w')
    writer = csv.writer(fp, delimiter = ',')
    for k in lst:
        writer.writerow(k)
 
def inpt():
    b=[]
    g=[]
    bn=[]
    gn=[]
    for i in range(0,30):
        bn.append('B'+chr(random.randrange(97, 123))+chr(random.randrange(97, 123)))
    for i in range(0,30):
        gn.append('G'+chr(random.randrange(97, 123))+chr(random.randrange(97, 123)))
    #print(bn)
    #print (gn)
    for i in range(0,26):
        b=b+[(bn[i],random.randint(0,500), random.randint(0,500), random.randint(0,500), random.randint(0,500))]
    for j in range(0,20):
        g=g+[(gn[j],random.randint(0,500), random.randint(0,500), random.randint(0,500))]
    #print(b)
    #print (g)
    csvfile('./b.csv',b)
    csvfile('./g.csv',g)
        
#inpt()
