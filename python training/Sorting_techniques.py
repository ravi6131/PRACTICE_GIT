import sys

def bubblesort(listvalues):
    for i in range(len(listvalues)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=a
                

#Selection Sort

def selection_sort(l):
    for i in range(len(l)-1):
        key=i
        for j in range(i,len(l)-1):
            if l[j]<l[key]:
                key=j
        temp=l[i]
        l[i]=l[key]
        l[key]=temp
    
    print(l)
    


def intersection_sort(data):
    for i in range(1,len(data)-1):
        key=data[i]
        j=i-1
        while j>=0 and key<data[j]:
            data[j+1]=data[j]
            j=j-1
        data[j+1]=key
    print(data)
intersection_sort([5,3,6,2,7,8])
        
def quick_sort(data):
    if len(data)<2:
        return data
    
    low,same,high=[],[],[]
    pivot=data[-1]
    
    for i in data:
        if pivot==i:
            same.append(i)
        elif pivot<i:
            low.append(i)
        elif pivot>i:
            high.append(i)
    return quick_sort(low)+same+quick_sort(high)

print(quick_sort([6,1,4,2,3]))




def triplet(data):
    for i in range(len(data)):
        data[i]=data[i]*data[i]
    data.sort()
    
    for i in range(len(data)-1,1,-1):
        l=0
        r=i-1
        while(l<r):
            if data[l]+data[r]==data[i]:
                print("triplet FOund")
                print(data[l],data[r],data[i])
                break
            elif(data[l]+data[r]<data[i]):
                l=l+1
            elif(data[l]+data[r]>data[i]):
                r=r-1
triplet([2,3,4,5])


import sys
 
stdin_fileno = sys.stdin
 
# Keeps reading from stdin and quits only if the word 'exit' is there
# This loop, by default does not terminate, since stdin is open
for line in stdin_fileno:
    # Remove trailing newline characters using strip()
    if 'exit' == line.strip():
        print('Found exit. Terminating the program')
        exit(0)
    else:
        print('Message from sys.stdin: ---> {} <---'.format(line))


#Queues using Stacks

-->Enqueue
    Push all elements s1 to s2
    Now adding new_element to s1.
    Copying all elements s2 to s1
-->Dequeue
    If stack empty error
    removing last element from s1
    Now return 
    