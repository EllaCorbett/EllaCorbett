#def BubbleSort(numbers):
#    print("Number of steps of BBS is", step)
def BubbleSort(numbers):
    for position in range (len(numbers)-1,-1,-1):
        for j in range(position):
            if numbers[j]>numbers[j+1]:
                temp=numbers[j]
                numbers[j]=numbers[j+1]
                numbers[j+1]=temp

def BubbleSort2_DESC(numbers):
    for position in range (0, len(numbers)-1):
        for j in range(len(numbers)-1, position, -1):
            if numbers[j]> numbers[j-1]:
                temp=numbers[j]
                numbers[j]=numbers[j-1]
                numbers[j-1]=temp

def BubbleSort_DESC(numbers):
    for position in range (len(numbers)-1,-1,-1):
        for j in range(position):
            if numbers[j]<numbers[j+1]:
                temp=numbers[j]
                numbers[j]=numbers[j+1]
                numbers[j+1]=temp

def SelectionSort(numbers):
    for position in range (len(numbers)-1,-1,-1):
        maxindex=position
        for j in range(position):
            if numbers[maxindex]<numbers[j]:
                maxindex=j
        temp=numbers[maxindex]
        numbers[maxindex]=numbers[position]
        numbers[position]=temp
        
            