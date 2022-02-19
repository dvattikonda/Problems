import random
import time
import matplotlib.pyplot as plt

def testingprogram():
    numbers = []
    for i in range(int(items_in_list)):
        numbinlist = random.randint(1, 1000)
        numbers.append(numbinlist)
    print(numbers)
    return numbers


def sorted(numbers):
    lenght = len(numbers)
    for i in range(lenght - 1):
        numb = i
        for ii in range(i + 1, lenght):
            # i + 1 excludes the numbers that are already sorted
            if numbers[ii] < numbers[numb]:
                numb = ii

        if numb != i:
            sortednumber = numbers[i]
            numbers[i] = numbers[numb]
            numbers[numb] = sortednumber
    return numbers


# Making the Graph
x = [0]
y = [0]
z = []
a = []
items_in_list = 2
for ii in range(10):
        items_in_list = items_in_list * 2
        numbers = testingprogram()
        start = time.time()
        s=sorted(numbers)
        end = time.time()
        print(s)
        timetaken = end - start
        x.append(items_in_list)
        y.append(timetaken)
        z.append(end)
        plt.plot(x, y)

plt.xlabel('# of numbers in list')
plt.ylabel('Time to sort lists')
plt.title('Graph for Selection Sorting')
plt.show()

plt.clf()
print("******************************************")
x2 = [0]
y2 = [0]
number_of_lists = 1
for ii in range(10):
    items_in_list = 10
    number_of_lists = number_of_lists * 2
    start = time.time()
    for j in range(number_of_lists):
        numbers = testingprogram()
        s = sorted(numbers)
        end = time.time()
    timetaken = end - start
    x2.append(number_of_lists)
    y2.append(timetaken)
    plt.plot(x2, y2)


plt.xlabel('# of lists')
plt.ylabel('Time to sort lists')
plt.title('# of lists vs. time to sort lists')

plt.show()