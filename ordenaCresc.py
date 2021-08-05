list1=[1245,456033,7,1,345,15,20,0]
list2=['a','b','c','d','e','f','g','h']
 
print ("Num original: "+str(list1))
print ("Letter original: "+str(list2))
 
print('\n')
 
flag = True
 
while (flag):
    flag = False
    for i in range(len(list1)-1):
        if (list1[i] > list1[i+1]):
            aux1 = list1[i+1]
            list1[i+1] = list1[i]
            list1[i] = aux1
            
            aux2 =list2[i+1]
            list2[i+1] = list2[i]
            list2[i] = aux2
            
            flag = True
 
print ("Nums sorted: "+str(list1))
print ("Letters sorted: "+str(list2))
