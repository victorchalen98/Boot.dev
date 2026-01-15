def tsp(cities, paths, dist):
    all_routes = permutations(cities)

    for route in all_routes:          
        total = 0

        for i in range(len(route) - 1):   
            from_city = route[i]
            to_city = route[i + 1]
            total += paths[from_city][to_city]

            if total >= dist:
                break

        if total < dist:
            return True

    return False

# don't touch below this line

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

