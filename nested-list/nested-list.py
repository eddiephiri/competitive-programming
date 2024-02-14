if __name__ == '__main__':
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    temp = [x for x in sorted_scores if x[1] > sorted_scores[-1][1]]
    
    final = sorted([i for i in temp if i[1] == temp[-1][1]], key=lambda x: x[0])
    
    for i in final:
        print(i[0])
