def ArithGeo(arr):
    diff_arr = []
    div_arr = []
    i = 0
    while (i<len(arr)-1):
        diff_arr.append(arr[i + 1] - arr[i])
        div_arr.append(arr[i + 1] // arr[i])
        i += 1


    if len(set(diff_arr)) == 1:
        return "Arithmetic"

    elif len(set(div_arr)) == 1:
        return "Geometric"
    else:
        return "-1"

print(ArithGeo([5, 10, 15]))