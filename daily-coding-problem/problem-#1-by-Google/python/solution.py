def solution(list_nums, target):
    # use a set to cache the number we have seen.
    cache = set()
    for num in list_nums:
        if target - num in cache:
            return True
        else:
            cache.add(num)
    return False


def main():
    test_list = [10, 15, 3, 7]
    k = 17
    print(solution(test_list, k))


if __name__ == '__main__':
    main()
