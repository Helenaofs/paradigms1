def sort_list_imperative(numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if (numbers[j] < numbers[j + 1]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

nums = [1, 3, 7, 8, 4, 2, 6, 5]
print(sort_list_imperative(nums))

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

print(sort_list_declarative(nums))