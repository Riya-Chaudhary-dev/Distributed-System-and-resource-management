m1 = [0,1,1]
m2 = [1,1,2]

counter = 0
eqcount =0 
for index in range(len(m1)):
    if(m1[index]<m2[index]):
        counter+=1
    elif(m1[index]>m2[index]):
        counter-=1
    else:
        eqcount +=1
if(abs(counter)==len(m1)-eqcount):
    if(counter>0):
        print('M1 is older than M2')
    else:
        print('M2 is younger than M2')
else:
    print('M1 and M2 are Concurrent')