import fnmatch

def audit(response):
    req = []
    f = open('babson_requirements.csv')
    for line in f:
        line = line.split()
        req.append(line)

    remaining = []
    classes = response.split()
    have = classes
    needed = req

    for code_lst in needed:
        is_present = False
        for requirement in code_lst:
            if requirement in have or fnmatch.filter(have, requirement):
                is_present = True

                for i in range(len(have)):
                    if [have[i]] == (fnmatch.filter([have[i]], requirement)):
                        have = have[:i]+ have[i+1:]
                        break
                    break
        if is_present == False:
            remaining.append(code_lst)

    return remaining
