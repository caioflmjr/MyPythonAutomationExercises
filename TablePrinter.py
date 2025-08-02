def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i, l_interna in enumerate(tableData):
        colWidths[i] = max(len(s) for s in l_interna)

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(f"{tableData[j][i].rjust(colWidths[j])}", end=' ')
        print('')

# --- Exemplo de Uso ---
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)