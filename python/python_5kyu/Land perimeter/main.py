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
for str in arr:
    for char in str:
        temp_list.append(True if char == "X" else False)
        if char == "X":
            perimeter += 4
    bool_lists.append(temp_list)
    temp_list = []

row_max_index = len(bool_lists[0]) - 1
col_max_index = len(bool_lists) - 1

# subtract 1 for every adjacent True registered
for row in bool_lists:
    row_index = bool_lists.index(row)
    for i in row:
        if row[i] == True:
            if row[i + 1] == True and (i + 1) <= row_max_index:
                perimeter -= 1
            if row[i - 1] == True and (i - 1) >= 0:
                perimeter -= 1
            if row_index + 1 <= col_max_index:
                if bool_lists[row_index + 1][i] == True:
                    perimeter -= 1
            if row_index - 1 > 0:
                if bool_lists[row_index - 1][i] == True:
                    perimeter -= 1

print(perimeter)



def main() -> None:
    pass

if __name__ == "__main__":
    main()