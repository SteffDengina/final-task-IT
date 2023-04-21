def sort(lst):
    for i in range(1, len(lst)):
        current_val = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current_val:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = current_val
    return lst

nums = input("Введите числа через запятую: ")
nums_lst = [int(num) for num in nums.split(",")]
sorted_lst = sort(nums_lst)
print("Отсортированный список:", sorted_lst)