def keys_data():
    keys = []

    fileHandler = open('./docProcKeysData.txt', 'r', encoding='utf-8')
    lines = fileHandler.readlines()
    fileHandler.close()
    l = []
    for line in lines:
        if line == '\n':
            if len(l) != 0:
                keys.append(l)
                l = []
        else:
            l.append(line)
    keys.append(l)
    return keys


def para_data(n=-1):
    paras = []

    fileHandler = open('./docProcParaData.txt', 'r', encoding='utf-8')
    lines = fileHandler.readlines()
    fileHandler.close()
    l = []
    for line in lines:
        if line == '\n':
            if len(l) != 0:
                paras.append(l)
                l = []
        else:
            l.append(line)
    paras.append(l)

    if n < 0:
        return paras
    else:
        return paras[n]
