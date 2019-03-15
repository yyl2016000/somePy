a_str = "babad"
max_length = 0
out_a_str = ""
if len(a_str) == 1:
    out_a_str = a_str
else:
    for i in range(len(a_str)):
        for j in range(i+1,len(a_str)):
            if list(a_str[i:j]) == list(reversed(a_str[i:j])):
                if (j-i) > max_length:
                    out_a_str = a_str[i:j]
                    max_length = (j-i)
print(out_a_str)