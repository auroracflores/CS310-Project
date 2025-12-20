def mergeTrack(arr, left, mid, right):
    sub1 = mid - left + 1
    sub2 = right - mid

    L = [0] * sub1
    R = [0] * sub2

    for i in range(sub1):
        L[i] = arr[left + i]
    for j in range(sub2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < sub1 and j < sub2:
        if L[i].track_name <= R[j].track_name:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < sub1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < sub2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeArtist(arr, left, mid, right):
    sub1 = mid - left + 1
    sub2 = right - mid

    L = [0] * sub1
    R = [0] * sub2

    for i in range(sub1):
        L[i] = arr[left + i]
    for j in range(sub2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < sub1 and j < sub2:
        if L[i].artist <= R[j].artist:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < sub1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < sub2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeEnergy(arr, left, mid, right):
    sub1 = mid - left + 1
    sub2 = right - mid

    L = [0] * sub1
    R = [0] * sub2

    for i in range(sub1):
        L[i] = arr[left + i]
    for j in range(sub2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < sub1 and j < sub2:
        if L[i].energy <= R[j].energy:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < sub1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < sub2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, left, right, sortChoice):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid, sortChoice)
        mergeSort(arr, mid + 1, right, sortChoice)
        sortChoice(arr, left, mid, right)
        #How to call each function:
        # mergeSort(arr, 0, len(arr)-1, mergeTrack)
        # mergeSort(arr, 0, len(arr)-1, mergeArtist)
        # mergeSort(arr, 0, len(arr)-1, mergeEnergy)
