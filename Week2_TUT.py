def bitCount(stringCount):
    for i in range(64):
        if(2**i >= stringCount):
            return i
        

print(bitCount(18))