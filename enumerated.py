# Enumeration by
# converting String list to ascii values
# using loop + ord()

# initialize list
test_list = [input("Enter Name or word:  ")]

# Convert String list to ascii values
# using loop + ord()
res = []
for ele in test_list:
    res.extend(ord(num) for num in ele)

enumerated = 0

for x in range(len(res)):
    enumerated += res[x]

sum_of_digits = sum(int(digit) for digit in str(enumerated))

sum_of_digits = sum(int(digit) for digit in str(sum_of_digits))
print(f"The checksum is: {sum_of_digits}")

if sum_of_digits == 2:
    print("Chokmah")
elif sum_of_digits == 3:
    print("Binah")
elif sum_of_digits == 4:
    print("Chesed")
elif sum_of_digits == 5:
    print("Geburah")
elif sum_of_digits == 6:
    print("Tipharet")
elif sum_of_digits == 7:
    print("Netzach")
elif sum_of_digits == 8:
    print("Hod")
else:
    print("Yesod")