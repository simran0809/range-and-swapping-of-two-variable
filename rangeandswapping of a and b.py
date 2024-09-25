for i in range(6):
    print(i)

    if i == 5: 
        i = i +1 # This condition will never be true because 'i' will only go from 0 to 3 in range(4)
        break

else:
    print("sorry i")
a = 5
b = 10

# Swapping without using a third variable
a = a + b  # Now a = 15
b = a - b  # Now b = 5
a = a - b  # Now a = 10

print("After swapping: a =", a, "b =", b)
