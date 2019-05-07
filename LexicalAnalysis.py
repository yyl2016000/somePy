#将输入的一行代码分解成关键字、界限符、运算符、标识符、常数
#如果不是标识符，则将其在对应表中的对应号一并输出
KeyWordTable = {"int":1, "long":2, "float":3, "double":4, "char":5, "for":6, "while":7, "continue":8, "break":9,
                "if":10,"else":11, "elif":12, "None":13, "return":14, "switch":15, "case":16, "pass":17, "and":18,
                "or":19, "not":20, "True":21, "False":22, "void":23}

DelimterTable = {"{":1, "}":2, "[":3, "]":4, "(":5, ")":6, " ":7, ":":8, ",":9, ";":10}

OperatorTable = {"+":1, "-":2, "*":3, "/":4, "%":5, "<":6, ">":7, "=":8, "+=":9, "-=":10, "!=":11, "<=":12, ">=":12,
                 "//":13, "!":14}

in_str = input("Please input a line code:")
out_list = []
#out_list为结果列表，以", "作为分界符
s = 0
while s < len(in_str):
#for s in range(len(in_str)):
    if in_str[s] in DelimterTable:
        out_list.append(in_str[s] +", 界限符, "+str(DelimterTable[in_str[s]]))
        s += 1
        continue
    elif in_str[s] in OperatorTable:
        # if in_str[s] == '-':
        #     end = s + 1
        #     if end == len(in_str):
        #         s = end
        #         out_list.append("ERROR 005")  # 负号后不能换行
        #         break
        #     while end < len(in_str) and ('0' <= in_str[end] <= '9'):
        #         end += 1
        #     if end == len(in_str) or in_str[end] == ' ' or in_str[end] in OperatorTable:
        #         out_list.append(in_str[s:end] + ", 负整数, " + "DEFAULT")
        #         s = end
        #         continue
        #     elif in_str[end] == '.':
        #         if end == s+1:
        #             s = end
        #             out_list.append("ERROR 004")  # 负号后不能加点
        #             break
        #         end += 1
        #         if end == len(in_str):
        #             s = end
        #             out_list.append("ERROR 001")  # 小数点不能换行
        #             break
        #         while end < len(in_str) and ('0' <= in_str[end] <= '9'):
        #             end += 1
        #         if end == len(in_str) or in_str[end] == ' ' or in_str[end] in OperatorTable:
        #             out_list.append(in_str[s:end] + ", 负浮点数, " + "DEFAULT")
        #             s = end
        #             continue
        #         else:
        #             s = end
        #             out_list.append("ERROR 002")  # 小数不能出现其他字符
        #             break
        #     else:
        #         s = end
        #         out_list.append("ERROR 003")  # 整数不能出现其他字符
        #         break
        if in_str[s:s+2] in OperatorTable:
            out_list.append(in_str[s:s+2] + ", 双目运算符, " + str(OperatorTable[in_str[s:s+2]]))
            s += 2
            continue
        else:
            out_list.append(in_str[s] + ", 运算符, " + str(OperatorTable[in_str[s]]))
            s += 1
            continue
    elif 'a' <= in_str[s] <= 'z' or 'A' <= in_str[s] <= 'Z' or in_str[s] == '_':
        end = s+1
        while end < len(in_str) and ('a' <= in_str[end] <= 'z' or 'A' <= in_str[end] <= 'Z' or '0'<= in_str[end] <= '9' or in_str[end] == '_'):
            end += 1
        if in_str[s:end] in KeyWordTable:
            out_list.append(in_str[s:end] + ", 关键字, " + str(KeyWordTable[in_str[s:end]]))
            s = end
            continue
        else:
            out_list.append(in_str[s:end] + ", 自定义标识符, " + "DEFAULT")
            s = end
            continue
    elif '0'<= in_str[s] <= '9':
        end = s + 1
        while end < len(in_str) and ('0'<= in_str[end] <= '9'):
            end += 1
        if end == len(in_str) or in_str[end] in DelimterTable or in_str[end] in OperatorTable:
            out_list.append(in_str[s:end] + ", 整数, " + "DEFAULT")
            s = end
            continue
        elif in_str[end] == '.':
            end += 1
            if end == len(in_str):
                s = end
                out_list.append("ERROR 001")#小数点不能换行
                break
            while end < len(in_str) and ('0' <= in_str[end] <= '9'):
                end += 1
            if end == len(in_str) or in_str[end] in DelimterTable or in_str[end] in OperatorTable:
                out_list.append(in_str[s:end] + ", 浮点数, " + "DEFAULT")
                s = end
                continue
            else:
                s = end
                out_list.append("ERROR 002")#小数不能出现其他字符
                break
        else:
            s = end
            out_list.append("ERROR 003")#整数不能出现其他字符
            break
print(out_list)