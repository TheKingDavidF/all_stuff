
def climbingLeaderboard1(ranked, player):
    results = []
    for score in player:
        new_ranked = ranked + [score]
        unique_new_ranked = list(set(new_ranked))
        sorted_unique_new_ranked = sorted(unique_new_ranked, reverse=True)
        # print('new_ranked: {}; unique_new_ranked: {}; sorted_unique_new_ranked: {};'
        #       .format(new_ranked, unique_new_ranked, sorted_unique_new_ranked))
        results.append(sorted_unique_new_ranked.index(score) + 1)
    return results


def climbingLeaderboard(ranked, player):
    results = []
    ranked_index = len(ranked) - 1
    current_rank = len(set(ranked)) + 1
    for score in player:
        if current_rank == 2:
            if ranked[0] <= score:
                results.append(1)
                continue
        while ranked[ranked_index] <= score and ranked_index >= 0:
            ranked_index -= 1
            if ranked[ranked_index] != ranked[ranked_index + 1]:
                current_rank -= 1
        results.append(current_rank)


    return results




ranked = list(map(int, '100 100 50 40 40 20 10'.split()))
player = list(map(int, '5 25 50 120'.split()))

ranked1 = list(map(int, '100 90 90 80 75 60'.split()))
player1 = list(map(int, '50 65 77 90 102'.split()))
ranked2 = [1]
player2 = [1, 1]

print(climbingLeaderboard(ranked2, player2))
