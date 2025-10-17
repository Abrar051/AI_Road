x = ['A', 'B', 'C', 'D']
D = ['Red', 'Green', 'Blue' , 'Black']


def CreateTouple(list1, list2):
    return (list1[0], list2[0])


def FollowConstraint(list1, list2):
    constraintDictionary = {}
    for i in list1:  # running loop for list1
        for j in list2:
            if not i in constraintDictionary: # and j != constraintDictionary[i]:
                constraintDictionary[i] = j
                list2.remove(j)


    return constraintDictionary


print(FollowConstraint(x, D))
