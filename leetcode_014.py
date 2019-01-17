strs = list(map(str,input().split()))

if len(strs) >= 1:
    min_len = len(strs[0])
    for tmp_str in strs:
        min_len = len(tmp_str) if(len(tmp_str) < min_len) else min_len
    out_str = ""
    for i in range(min_len):
        flag = 1
        flag_char = strs[0][i]
        for j in range(len(strs)):
            if strs[j][i] != flag_char :
                flag = 0
                break
        if flag:
            out_str += strs[0][i]
        else:
            break
    print(out_str)
else:
    print("")