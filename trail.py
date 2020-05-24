num = int(input())

lst = []
count  = 0
maxi = 0
while(num>0):
    lst.append(num%2)
    num = int(num/2)

for i in range(0,len(lst)):
    if(lst[i]==0):
        count+=1
    else:
        count = 0
    if(count>=maxi):
        maxi = count
        
print(maxi)
