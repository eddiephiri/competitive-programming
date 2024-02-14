if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = sorted(arr, reverse=True)
    print([x for x in sorted_arr if x < sorted_arr[0]][0])
