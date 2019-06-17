def main(a :str, b: str) -> str:
    la,lb = len(a), len(b)
    ta,tb = a,b
    if la < lb:
        ta,tb = tb,ta
        la,lb = lb,la
    bu = la-lb
    up = '0'
    out_str=[]
    for i in range(lb-1,-1,-1):
        boolean = ta[i+bu] != tb[i]
        if boolean:
            if up == '1':
                out_str.append('0')
                up = '1'
            else:
                out_str.append('1')
                up = '0'
        else:
            out_str.append(up)
            if ta[i+bu] and tb[i] == '1':
                up = '1'
            else:
                up = '0'
    for i in range(la-lb-1,-1,-1):
        if up == '0':
            out_str.append(ta[i])
        else:
            if ta[i] == '0':
                out_str.append('1')
                up = '0'
            else:
                out_str.append('0')
                up = '1'
    if up == '1':
        out_str.append('1')
    out_str.reverse()
    return "".join(out_str)
if __name__ == '__main__':
    a = input('输入a的值')
    b = input('输入b的值')
    print(main(a, b))