def solution(friends, gifts):
    member_map = {name: i for i, name in enumerate(friends)}
    l = len(friends)
    gift_gragh = [[0] * l for _ in range(l)]

    for gift_info in gifts:
        giver, taker = gift_info.split()
        gift_gragh[member_map[giver]][member_map[taker]] += 1

    member_total_give = [0] * l
    member_total_take = [0] * l
    for i in range(l):
        member_total_give[i] = sum(gift_gragh[i])
        member_total_take[i] = sum([k[i] for k in gift_gragh])

    member_gift_score = [member_total_give[i] - member_total_take[i] for i in range(l)]

    member_next_give = [0] * l
    for i in range(l):
        for j in range(i+1, l):

            if gift_gragh[i][j] > gift_gragh[j][i]:
                member_next_give[i] += 1
            elif gift_gragh[i][j] < gift_gragh[j][i]:
                member_next_give[j] += 1
            else:
                if member_gift_score[i] > member_gift_score[j]:
                    member_next_give[i] += 1
                elif member_gift_score[i] < member_gift_score[j]:
                    member_next_give[j] += 1
                else:
                    continue

    return max(member_next_give)


result = solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
print(result)
