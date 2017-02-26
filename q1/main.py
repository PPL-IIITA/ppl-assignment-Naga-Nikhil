from girl import girl
from boy import boy
from input import inpt
import csv
from logfile import funcn


inpt()
fileb=open('./b.csv')
b = csv.reader(fileb, delimiter = ',')
fileg=open('./g.csv')
g = csv.reader(fileg, delimiter = ',')
boys=[]
girls=[]
for i in b:
    if i!=[]:
        print (i)
        boys+=[boy(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]))]
for j in g:
    if j!=[]:
        print (j)
        girls += [girl(j[0], int(j[1]), int(j[2]), int(j[3]))]

for girlobj in girls:
    for boyobj in boys:
        if boyobj.is_elligible(girlobj) and girlobj.is_elligible(boyobj) and girlobj.status=='single' and boyobj.status=='single':
            girlobj.bf=boyobj.name
            boyobj.gf=girlobj.name
            girlobj.status = 'commited'
            boyobj.status= 'commited'
            print(boyobj.name+ ' is in relationship with ' +girlobj.name)
            funcn(boyobj.name + ' is in relationship with ' + girlobj.name)
            break
