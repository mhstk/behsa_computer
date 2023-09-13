def next(num, map):
    if num > len(map)+1 or num < 1:
        print("HEREEEEE")
        return -1
    # print('ddddd', num)
    next = num + int(map[num-1])
    if next == -1:
        print("inja")
    # print(next)
    return next


def cal(num, map, maxx):
    step = 0
    curr = num
    see = []

    while step <= maxx:
        
        new = next(curr, map)
        see.append(curr)
        
        step += 1
        if new == -1:
            print("ssssssss")
            return -1
        if new in see:
            print("DDDDDD")
            return -1
        print(curr, new, step)
        curr = new
        if curr == len(map)+1 or curr == len(map):
            # print("SUCCC")
            return step
        # print(curr)
    
    print("HHHHHHH")
    return -1

    


def turn(map, maxx):
    ans = None
    for i in range(len(map)):
        # print(i)
        
        step = cal(i+1, map, maxx) 
        # print(i, step, len(map))
        if step != -1:
            # print(i, step, (i+1)*(step+1) )
            if ans:
                if step > ans[0]:
                    ans = (step, (i+1)*(step+1))
            else: 
                ans = ( step, (i+1)*(step+1))
        # input()
    print()
    print()
    print(ans)

    



map = input().split(',')
maxx = len(map)*len(map)*len(map)*len(map)*len(map)*len(map)
print(map)
turn(map, maxx)
