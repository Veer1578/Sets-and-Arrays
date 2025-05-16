tp = {1, 2, 3}
print(tp)

tp = {1.0, 'Hey', (1, 2, 3)}
print(tp)

tp = {1, 2, 3, 4, 4, 3, 2, 1}
print(tp)

tp = set([1, 2, 3])
print(tp)

og = set([0, 1, 2, 3, 4, 5])
print('The orignal set:')
print(og)
og.pop()
print('After removing first element:')
print(og)