# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python

arr = ['XOOXO',
       'XOOXO',
       'OOOXO',
       'XXOXO',
       'OXOOO']

arr2 = ["OXOOOX", 
        "OXOXOO", 
        "XXOOOX", 
        "OXXXOO", 
        "OOXOOX", 
        "OXOOOO", 
        "OOXOOX", 
        "OOXOOO", 
        "OXOOOO", 
        "OXOOXX"]

temp_list = []
bool_lists =[]
perimeter = 0

# Add 4 to perimeter for every True
for str in arr2:
    for char in str:
        temp_list.append(True if char == "X" else False)
        if char == "X":
            perimeter += 4
    bool_lists.append(temp_list)
    temp_list = []

row_max_index = len(bool_lists[0]) - 1
col_max_index = len(bool_lists) - 1

print(perimeter)

# subtract 1 for every adjacent True registered
for row_index, row in enumerate(bool_lists, start = 0):
    for index, i in enumerate(row, start=0):
        if row[index] == True:
            try:
                if row[index + 1] == True:
                    perimeter -= 1
            except:
                pass
            try:
                if row[index - 1] == True:
                    perimeter -= 1
            except:
                pass
            try:
                if bool_lists[row_index - 1][index] == True:
                    perimeter -= 1
            except:
                pass
            try:
                if bool_lists[row_index + 1][index] == True:
                    perimeter -= 1
            except:
                pass

return f"Total land perimeter: {perimeter}"



def main() -> None:
    pass

if __name__ == "__main__":
    main()