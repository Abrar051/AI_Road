import numpy as np

listItem = [
  {"x": 5,  "y": 5,  "c": "red"},
  {"x": 10, "y": 10, "c": "blue"},
  {"x": 15, "y": 5,  "c": "green"}
]

def gowerDistance (listItem):
    n = len(listItem)
    distanceMatrix = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            sumDiff = 0
            attrCount = 0
            for key in listItem[i].keys():
                if isinstance(listItem[i][key], (int, float)) and isinstance(listItem[j][key], (int, float)):
                    diff = abs(listItem[i][key] - listItem[j][key])
                    rangeAttr = max([item[key] for item in listItem]) - min([item[key] for item in listItem])
                    if rangeAttr != 0:
                        normDiff = diff / rangeAttr
                    else:
                        normDiff = 0
                    sumDiff += normDiff
                    attrCount += 1
                elif isinstance(listItem[i][key], str) and isinstance(listItem[j][key], str):
                    if listItem[i][key] == listItem[j][key]:
                        sumDiff += 0
                    else:
                        sumDiff += 1
                    attrCount += 1
            if attrCount > 0:
                distanceMatrix[i][j] = sumDiff / attrCount
            else:
                distanceMatrix[i][j] = 0
    return distanceMatrix

print(gowerDistance(listItem))

