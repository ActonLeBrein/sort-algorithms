def bucket_sort(lst):
    bucket, bucket1, bucket2 = [], [], [] #The three empty buckets
    #Populating the buckets with the list elements
    for i in range(len(lst)):
        if lst[i] in range(11):
            bucket.append(lst[i])
        elif lst[i] in range(21):
            bucket1.append(lst[i])
        elif lst[i] in range(31):
            bucket2.append(lst[i])
            
    #Prints the buckets and their contents
    print "Bucket:",bucket
    print "Bucket1:",bucket1
    print "Bucket2:",bucket2
    #The actual sorting 
    bucket.sort()
    bucket1.sort()
    bucket2.sort()
    final_lst = bucket + bucket1 + bucket2
    print "Sorted list:",final_lst
    
a = [5,81,2,53,0,4,655,7,99]
print bucket_sort(a)