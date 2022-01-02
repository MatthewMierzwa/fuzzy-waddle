def sort_array(source_array):
    for i in range(0,len(source_array)-1):
        id=i
        if source_array[i]%2==0:
            continue
        else:
            min=source_array[i]
        for j in range(i+1,len(source_array)):
            if source_array[j]%2==0:
                continue
            else:
                if source_array[j]<min:
                    id=j
                    min=source_array[j]
        temp=source_array[i]
        source_array[i]=min
        source_array[id]=temp
    return source_array
