import random
import copy
import math

N = 80  # 全員の数
M = 5  # グループのメンバー数
T = 5  # ミーティングの回数
TRY_NUM = 40000  # 試行数


def init_score_boards() -> list[list[int]]:
    board = []
    for i in range(N):
        board.append([0 for j in range(N)])
    return board

# 5 x 16の配列を返す


def get_random_groups() -> list[list[int]]:
    members = [i for i in range(N)]
    groups = []
    random.shuffle(members)
    group = []
    count = 0
    for m in members:
        count += 1
        group.append(m)
        if count % M == 0:
            groups.append(group)
            group = []

    return groups

# 5 x 16 の配列をscore_boardに足し上げる


def add_to_score_boards(boards: list[list[int]], groups: list[list[int]]) -> list[list[int]]:
    new_boards = copy.deepcopy(boards)
    for group in groups:
        for member in group:
            host_score_arr = new_boards[member]
            for partner_idx in range(M):
                partner = group[partner_idx]
                if member == partner:
                    continue
                host_score_arr[partner] = host_score_arr[partner] + 1
            new_boards[member] = host_score_arr

    return new_boards

# 5 x 16 の配列 + スコア配列からsum_scoreを計算


def get_sum_score(board: list[list[int]]):
    score = 0
    for host_score_arr in board:
        # 重みづけロジックはよしなに

        # あるメンバーが同一人物と2回meetingする回数を減らす
        if host_score_arr.count(2) == 2:
            score = score + 30
        elif host_score_arr.count(2) == 3:
            score = score + 100
        elif host_score_arr.count(2) >= 4:
            score = score + 10000

        # 同じ人と複数回meetingする回数を減らす
        for meeting_count in host_score_arr:
            if meeting_count == 5:
                score = score + 1000000
            if meeting_count == 4:
                score = score + 500000
            elif meeting_count == 3:
                score = score + 120
            elif meeting_count == 2:
                score = score + 10

    return score


min_group_history = []
for i in range(M):
    min_group_history.append([])
min_score_board = []
min_group_score = math.inf

for i in range(TRY_NUM):
    score_board = init_score_boards()

    group_history = []
    for i in range(T):
        group = get_random_groups()
        score_board = add_to_score_boards(
            score_board,
            group
        )
        group_history.append(group)
    score = get_sum_score(score_board)
    print(f'score: {score}')

    if score < min_group_score:
        print('======score_updating===============')
        min_group_history = group_history
        min_group_score = score
        min_score_board = score_board


print('========score_board=============')
print(min_score_board)
print(f'score: {min_group_score}')

print('========groups=============')
for i in range(T):
    print(f'=={i}回==')
    print(min_group_history[i])
