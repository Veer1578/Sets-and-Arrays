import array as arr

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print(f'Orignal array: {str(array_num)}')

print(f'The no.of times 3 occured is {str(array_num.count(3))}')

array_num.reverse()
print(f'The reverse order is {array_num}')