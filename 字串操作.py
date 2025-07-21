#q182. 2. 字串操作
#https://zerojudge.tw/ShowProblem?problemid=q182
def switch0(word):
    word_list = list(word)
    word_a = word_list[::2]
    word_b = word_list[1::2]
    pair = list(zip(word_a,word_b)) 
    swapped_list = []
    for a, b in pair:
        swapped_list.append(b)  
        swapped_list.append(a)
    swapped = "".join("".join(map(str,h)) for h in swapped_list)
    return swapped
def switch1(word):
    word_list = list(word)
    word_a = word_list[::2]
    word_b = word_list[1::2]
    pair = list(zip(word_a,word_b))
    sorted_pair = [sorted(list(o)) for o in pair]   
    swapped = "".join("".join(map(str,h)) for h in sorted_pair)
    return swapped
def switch2(word):
    word_list = list(word)
    word_a = word_list[0:len(word_list)//2]
    word_b = word_list[len(word_list)//2:len(word_list)]
    swapped_list = []
    for a in range((len(word_list))//2):
        swapped_list.append(word_a[a])
        swapped_list.append(word_b[a])
    swapped = "".join("".join(map(str,h)) for h in swapped_list)
    return swapped
word = input()
k = int(input())
v = []
for i in range(k):
    number = int(input())
    v.append(number)
for j in v:
    if j == 0:
        word = switch0(word)
    if j == 1:
        word = switch1(word)
    if j == 2:
        word = switch2(word)
print(word)