def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i, l_interna in enumerate(tableData):
        maxlen = 0
        for str in l_interna:
            if len(str) > maxlen:
                colWidths[i] = maxlen = len(str)

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(f"{tableData[j][i].rjust(colWidths[j])}", end=' ')
        print('')