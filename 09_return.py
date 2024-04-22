def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth

def find_volume_2(length = 1, width = 1, depth = 1):
    return length * width * depth, width, 'string'

result = find_volume(2, 2, 3)

print(result)

result = find_volume()

print(result)

result = find_volume(width=39)

print(result)

result2 = find_volume_2(width=8)

print(result2)
print(result2[1])

volume, width, text = find_volume_2(width=8)

print(volume)
print(width)
print(text)