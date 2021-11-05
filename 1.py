even = []
odd = []


def calculator(a):
    for i in range(1, a + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)


number = int(input("Give a number: "))
calculator(int(number))
print("Sum of odd numbers , Average of even numbers: " , sum(odd) ,",", sum(even)/len(even))
