def addBinarystringusingonescompliment(a:str,b:str):
    max_length = max(len(a),len(b))

    a=a.zfill(max_length)
    b=b.zfill(max_length)

    result=""
    carry = 0

    for i in range(max_length-1,-1,-1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0

        result = ('1' if r%2 == 1 else '0') + result
        carry = 0 if r<2 else 1

    if carry != 0:
        result = addBinarystringusingonescompliment(result, '1')
    return result.zfill(max_length)

def complement(a:str):
    result = ''
    for i in a:
        result = result + ('0' if i == '1' else '1')
    return result

def calculateChecksum(frames:list):
    result = frames[0]

    for frame in frames[1:]:
        result = addBinarystringusingonescompliment(result, frame)

    result = complement(result)
    return result

print(complement('10101010'))
frames = ["11001", "01001", "11100", "00110", "10111"]
res = calculateChecksum(frames)
print(res)

frames.append(res)
res = calculateChecksum(frames)
print(res)
