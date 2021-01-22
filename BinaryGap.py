
def solution(N):
    # print(bin(N)[2:])
    zero_list = bin(N)[2:].split('1')
    sorted_list = sorted(zero_list, key=len, reverse=True)
    return len(sorted_list[0])


print(solution(435))

