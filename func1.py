def s_sum(l: list) -> int:
    ans = 0
    for i in l:
        ans += int(i)
    return ans


if __name__ == "__main__":

    assert s_sum([2,3,5,6]) == 16
    print(s_sum([2,3,5,6]))
    #---