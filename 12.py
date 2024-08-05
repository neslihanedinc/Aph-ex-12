def find_largest_second_number(numbers):
    if len(numbers) < 2:
        return None 
    largest = None
    second_largest = None
    for number in numbers:
        if largest is None or number > largest:
            second_largest = largest
            largest = number
        elif number != largest and (second_largest is None or number > second_largest):
            second_largest = number
    
    return second_largest

# Kullanıcıdan listeyi al
user_input = input("Enter a list of numbers (comma-separated): ")
number_strings = user_input.split(',')
numbers = []

# Dize elemanlarını tam sayıya dönüştür
for num_str in number_strings:
    numbers.append(int(num_str))

print("Numbers:", numbers)

# İkinci en büyük sayıyı bul ve yazdır
second_largest = find_largest_second_number(numbers)
print("Second largest number:", second_largest)
