if __name__ == '__main__':
    print("bootcamp")

    print("Hello World")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers[4])
    print(numbers[-4:-1])
    numbers.append(11)
    print(numbers)
    numbers[9] = 100
    print(numbers)
    x = numbers[0]
    print(x)
    for number in numbers:
        print(number)

    a = 10
    b = 5
    if a > b:
        print("a>b")
    elif a < b:
        print("a<b")
    else:
        print("a==b")

    if a % 2 == 0:
        print("a is even")
    else:
        print("a is odd")

    names = []
    print(names)
    names.append("John")
    print(names)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    print(even)

    for i in range(0, len(numbers),3):
        print(numbers[i])

    numbers = [7,8,9,10,1,2,3,5,4,6]
    max=numbers[0]
    min=numbers[0]
    for num in numbers:
        if num > max:
            max=num
        if num < min:
            min=num
    print(max)
    print(min)



    d={}
    d["a"]=5
    d["b"]=6
    print(d)
    d["a"]=d["a"]+1
    print(d)
    d["c"]=10
    d["c"]=11
    print(d)

    if x in d:
        print(d["a"])
    else: print("key does not exist in dictonary")


    numbers = [7,8,9,10,1,2,3,5,4,6,3,1,8]
    target=1
    count=0
    for num in numbers:
        if num == target:
            if num==target:
                count+=1
    print(count)

    numbers = [7, 8, 9, 10, 1, 2, 3, 5, 4, 6, 3, 1, 8]
    d={}
    for num in numbers:
        if num in d:
            d[num] = d[num] + 1
        else: d[num]=1
    print (d)

    numbers = [10,20,20,30]
    d={}
    for num in numbers:
        if num in d:
            d[num] = d[num] + 1
        else: d[num]=1
    print (d)


    freq=0
    max=0
    for key in d.keys():
        value=d[key]
        if value>freq:
            max=key
            freq=value
    print (max)

#finding most frequent word
    line = "hello world hi world hi nepal"
    words = line.split (' ')
    print (words)
    word_counts= {}
    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1
    print(word_counts)

    freq = 0
    word = 0
    for key in word_counts.keys():
        count = word_counts[key]
        if count > freq:
            word = key
            freq = count
    print (word)

#removing repeated num
    list=[1,2,2,3,4,4,5]
    s=set(list)
    print (s)

    list = [1, 2, 2, 3, 4, 4, 5]
    output=[]
    set=set()
    for num in list:
        if num not in output:
            output.append(num)
            set.add(num)
    print (output)

    output = [1,2,3,4,5]


    output =[]
    list = [1, 2, 2, 3, 4, 4, 5]   #use this approach in sorted input
    prev = list[0]
    output.append(prev)
    for num in list:
        if num != prev:
            output.append(num)
            prev=num
    print(output)

