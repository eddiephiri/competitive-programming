if __name__ == '__main__':
    N = int(input())
    data = []
    
    for _ in range(N):
        inpt_list = input().split()
        if len(inpt_list) > 1:
            if inpt_list[0] == 'insert':
                i = int(inpt_list[1])
                val = int(inpt_list[2])
                data.insert(i, val)
            elif inpt_list[0] == 'remove':
                i = int(inpt_list[1])
                data.remove(i)
            else:
                val = int(inpt_list[1])
                data.append(val)
        else:
            cmd = inpt_list[0]

            if cmd == 'print':
                print(data)
            elif cmd == 'pop':
                data.pop()
            elif cmd == 'sort':
                data.sort()
            else:
                data.reverse()
            
