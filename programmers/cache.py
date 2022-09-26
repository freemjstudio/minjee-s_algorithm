temp = {"Seoul":2, "NewYork":5}


def solution(cacheSize, cities):
    answer = 0
    cache = {}
    for city in cities:
        city = city.lower()
        if city in cache:
            cache[city] += 1
            answer += 1  # hit

        else:
            if len(cache) <= cacheSize:
                answer += 5  # miss
                cache[city] = 1

            else:
                # 가장 least recently used 를 pop 해야 함
                key = min(cache, key=cache.get)
                cache.pop(key)
                answer += 5
                cache[city] = 1

    return answer