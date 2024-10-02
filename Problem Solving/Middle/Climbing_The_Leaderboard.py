def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    result = []
    l = len(ranked)

    for score in player:
        while l > 0 and score >= ranked[l-1]:
            l -= 1
        result.append(l + 1)
        
    return result

#Example
ranked = [100, 90, 90, 80,75,60]
player = [50, 65,77,90, 105]

print(climbingLeaderboard(ranked, player)) 