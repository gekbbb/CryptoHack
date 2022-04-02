from operator import xor

def bytes2matrix(text):
    return [list(text[x:x+4]) for x in range(0, len(text), 4)]

def matrix2bytes(matrix):
    return [print(chr(y), end="") for sub in matrix for y in sub]

def add_round_key(source, key):
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for x in range(len(source)):
        for y in range(len(source)):
            result[x][y] = xor(source[x][y], key[x][y])
            
    return result

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

addKey = add_round_key(state, round_key)
matrix2bytes(addKey)