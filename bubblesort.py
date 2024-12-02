def BubbleSort(numbers):
    n=len(numbers)
    for i in range (n-1):
        for j in range (n-1,i,-1):
            if numbers [j]< numbers[j-1]:
                temp=numbers[j]
                numbers[j]= numbers[j-1]
                numbers[j-1]=temp

def smart_BubbleSort(numbers):
    step=0
    for posititon in range(len(numbers))