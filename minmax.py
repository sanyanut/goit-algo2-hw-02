def find_min_max(arr: list) -> tuple:
    if not arr:
        return None, None

    def dac_min_max(low: int, high: int) -> tuple:
        if low == high:
            return arr[low], arr[low]

        if high == low + 1:
            if arr[low] < arr[high]:
                return arr[low], arr[high]
            else:
                return arr[high], arr[low]

        mid = (low + high) // 2
        min1, max1 = dac_min_max(low, mid)
        min2, max2 = dac_min_max(mid + 1, high)

        return min(min1, min2), max(max1, max2)

    return dac_min_max(0, len(arr) - 1)

array = [3, 1, 9, 7, 5, -2, 8]
print(find_min_max(array))