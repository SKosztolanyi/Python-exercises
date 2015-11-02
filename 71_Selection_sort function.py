#Selection sort function
def selSort(L):
    for i in range(len(L)-1): ## I put there minus one, becase j is plus one.
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]: # In this step, minVals is L[i]
                minIndx = j
                minVal = L[j] # In this step, minVal is L[j] and is compared to another elements in list, reassigning the variable every time smaller element is found.
        # If j was smaller than i, it is assigned to variables minIndx and minVal.
        # If i was smaller than j, there is no reassignment.
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
        # With these last three lines I do an elements swap by changing indices of the values.
        # I create a temp variable to hold on to the "i" index, when I overwrite it with "j" index.
        # This way both values stay the same, they just change indices.
    return L