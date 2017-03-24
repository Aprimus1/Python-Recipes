

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

result = []

row_start = 0
row_end = len(array)
col_start = 0
col_end = len(array[0])


# right

for i in array[row_start][col_start:col_end]:
    print(i,end=' ')


# down

for i in array[row_start+1:row_end-1]:
    print(i[col_end-1],end=' ')

# left

for i in array[row_end-1][col_end-1:col_start:-1]:
    print(i, end=' ')

# up

for i in array[row_end-1:row_start:-1]:
    print(i[col_start], end=' ')
