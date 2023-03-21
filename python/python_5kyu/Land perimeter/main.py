# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python

arr = ['XOOXO',
       'XOOXO',
       'OOOXO',
       'XXOXO',
       'OXOOO']

def main() -> None:
    temp_list = []
    bool_lists =[]
    perimeter = 0

    # Convert array to True/False and add 4 to perimeter for every True
    for str in arr:
        for char in str:
            if char == "X":
                temp_list.append(True)
                perimeter += 4
            else:
                temp_list.append(False)
        bool_lists.append(temp_list)
        temp_list = []

    # Subtract 1 for every adjacent True
    for row in range(len(bool_lists)):
        for col in range(len(bool_lists[row])):
            if bool_lists[row][col]:
                # Check to right
                try:
                    if bool_lists[row][col + 1]:
                        perimeter -= 1
                except IndexError:
                    pass
                # Check to left
                if bool_lists[row][col - 1] and col - 1 >= 0:
                    perimeter -= 1
                # Check below
                try:
                    if bool_lists[row + 1][col]:
                        perimeter -= 1
                except IndexError:
                    pass
                # Check above
                if bool_lists[row - 1][col] and row - 1 >= 0:
                    perimeter -= 1


if __name__ == "__main__":
    main()
    # return f"Total land perimeter: {perimeter}"