def subset_string_recursion(string, out):
    if len(string) == 0:
        print(out)
        return

    # string을 other_out과 string으로 분리
    other_out = out + string[0]
    string = string[1:len(string)]

    subset_string_recursion(string, other_out)
    subset_string_recursion(string, out)


subset_string_recursion("qwerty", "")