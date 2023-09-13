
def next(num, map):
    if num > len(map) or num < 1:
        raise 'error'
    # print('ddddd', num)
    next = num + int(map[num-1])
    # print(next)
    return next


def cal(num, map, maxx):
    step = 0
    curr = num
    try:
        while step <= maxx:
            new = next(curr, map)
            step += 1
            curr = new
            if curr == len(map)+1:
                # print("SUCCC")
                return step
            # print(curr)
        return -1
    except:
        return -1
    


def turn(map, maxx):
    ans = None
    for i in range(len(map)):
        # print(i)
        step = cal(i+1, map, maxx) 
        if step != -1:
            print(i, step, (i+1)*(step+1) )
            if ans:
                if step > ans[0]:
                    ans = (step, (i+1)*(step+1))
            else: 
                ans = ( step, (i+1)*(step+1))
    print()
    print()
    print(ans)

    



map = input().split(',')
maxx = len(map)
print(map)
turn(map, maxx)
