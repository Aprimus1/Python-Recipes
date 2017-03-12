def flattener(lst):
    for i in lst:
        if isinstance(i,int):
            return i
        else:
            return flattener(i)

sequence = [[[1]],[2],[[3]], [[[[[[5]]]]]]]

y = map(flattener,sequence)

print y #[1,2,3,5]
