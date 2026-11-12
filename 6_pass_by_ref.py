def test(data):

    data.append(40)           # 1. Modify object (original)
    print(data ,(id(data)))

    data += [50]              # 2. In-place change (original, same object)
    print(data ,(id(data)))

    data = [100, 200]         # 3. Reassign parameter (data now points to a NEW list)
    print(data ,(id(data)))

    data.append(300)          # 4. Modify new object
    print(data ,(id(data)))

    data += [400]             # 5. In-place change on the new object
    data.append(300)          # 4. Modify new object
    print(data ,(id(data)))

numbers = [10, 20, 30]

test(numbers)

print(numbers)                # [10, 20, 30, 40, 50]
