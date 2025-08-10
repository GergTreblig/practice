#   Gregory Gilbert
#   8/9/2025
#   Practice with Fibonacci

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def bubble_sort(bubble_array):
    for i in range(len(bubble_array)):
        for j in range(len(bubble_array) - i - 1):
            if bubble_array[j] > bubble_array[j + 1]:
                bubble_array[j], bubble_array[j + 1] = bubble_array[j + 1], bubble_array[j]
    return bubble_array

def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
    return array

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('Bubble Sort')
    print(bubble_sort([5, 4, 3, 2, 1]))
    print(bubble_sort([5, 24, 30, 2, 12]))
    print('Merge Sort')
    print(merge_sort([5, 4, 3, 2, 1]))
    print(merge_sort([5, 24, 30, 12, 2]))
    print('Insertion Sort')
    print(insertion_sort([5, 4, 3, 2, 1]))
    print(insertion_sort([5, 24, 30, 12, 2]))
    print('Selection Sort')
    print(selection_sort([5, 4, 3, 2, 1]))
    print(selection_sort([5, 24, 30, 12, 2]))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
