def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(n):
        for j in range(len(flowerbed)):
            if j == 0 and flowerbed[j] == 0 and flowerbed[j+1] == 0:
                count += 1
                flowerbed[j] = 1
            elif j > 0 and flowerbed[j] == 0 and flowerbed[j-1] == 0 and flowerbed[j+1] == 0:
                count += 1
                flowerbed[j] = 1
    return count == n


print(canPlaceFlowers([1, 0, 0, 0, 1], 2))
