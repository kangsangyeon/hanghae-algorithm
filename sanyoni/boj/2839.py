required_weight = int(input())

can_devided = False
bag_3kg_count = 0
bag_5kg_count = required_weight // 5

while bag_5kg_count >= 0:
    remain_weight = required_weight - 5 * bag_5kg_count

    if remain_weight % 3 == 0:
        bag_3kg_count = remain_weight // 3
        can_devided = True
        break
    else:
        bag_5kg_count -= 1

if can_devided:
    print(bag_3kg_count + bag_5kg_count)
else:
    print(-1)