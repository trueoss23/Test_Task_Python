from datetime import datetime
from prettytable import PrettyTable
import json


def parsJsonFile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        dictName = json.load(f)
    return dictName


def parsTxtFile(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        result = {}
        for line in f:
            tempList = line.split()
            if tempList[1] == 'start':
                if tempList[0] in result:
                    result[tempList[0]] = getResultTime(tempList[2],
                                                        result[tempList[0]])
                else:
                    result[tempList[0]] = tempList[2]
            elif tempList[1] == 'finish':
                if tempList[0] in result:
                    result[tempList[0]] = getResultTime(result[tempList[0]],
                                                        tempList[2])
                else:
                    result[tempList[0]] = tempList[2]

    sorted_tuples = sorted(result.items(), key=lambda item: item[1])
    return sorted_tuples


def getResultTime(start, finish):
    start_ = datetime.strptime(start, '%H:%M:%S,%f')
    finish_ = datetime.strptime(finish, '%H:%M:%S,%f')
    return str(finish_ - start_)


def printResultTables(dictNames, sortedTupleDatesResults):
    table = PrettyTable()
    table.field_names = [
                    'Занятое место',
                    'Нагрудный номер',
                    'Имя',
                    'Фамилия',
                    'Результат'
                    ]
    for i, elem in enumerate(sortedTupleDatesResults):
        table.add_row([
                    i + 1,
                    elem[0],
                    dictNames[elem[0]]['Surname'],
                    dictNames[elem[0]]['Name'],
                    elem[1]
                    ])
    print(table)


if __name__ == '__main__':
    sortedTupleDatesResults = parsTxtFile('results_RUN.txt')
    dictNames = parsJsonFile('competitors2.json')
    printResultTables(dictNames, sortedTupleDatesResults)
