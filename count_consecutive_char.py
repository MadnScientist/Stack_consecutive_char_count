def count_consecutive_char(s):
    ss = list(s)
    ts = []
    v = ''
    for s in ss:
        if len(ts) == 0:
            print("add", s)
            ts.append(s)
        elif ts[-1] == s:
            print("add", s)
            ts.append(s)
        elif ts[-1] != s:
            print("clear ts, add new: ", s)
            v = v + str(ts[-1]) + str(len(ts))
            ts = []
            ts.append(s)
    if len(ts) > 0:
        v = v + str(ts[-1]) + str(len(ts))

    return v

count_consecutive_char("aaabbbac")
