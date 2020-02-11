
# Problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k


def equalTo(numbers,y):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            total_of_two_items = numbers[i] + numbers[j]
            if(total_of_two_items == y):
                print(numbers[i])
                print(numbers[j])
            else:
                print("false")






equalTo([10,15,3,7],17)
