def blackjack_hand_greater_than(hand_1, hand_2):
    hand_1_total = 0
    hand_2_total = 0
# This is for Hand 1
    for i in hand_1:
        if i in ("J","Q","K"):
            hand_1_total += 10
        elif i == "1":
            hand_1_total += 1
        elif i == "2":
            hand_1_total += 2
        elif i == "3":
            hand_1_total += 3
        elif i == "4":
            hand_1_total += 4
        elif i == "5":
            hand_1_total += 5
        elif i == "6":
            hand_1_total += 6
        elif i == "7":
            hand_1_total += 7
        elif i == "8":
            hand_1_total += 8
        elif i == "9":
            hand_1_total += 9
        elif i == "10":
            hand_1_total += 10

        
    
    for a in hand_1:
        if a == "A":
            if hand_1_total < 21 and (hand_1_total + 11) <= 21:
                hand_1_total += 11
            else:
                hand_1_total += 1
        else:
            continue
    

#This is for Hand 2
    for i in hand_2:
        if i in ("J","Q","K"):
            hand_2_total += 10
        elif i == "1":
            hand_2_total += 1
        elif i == "2":
            hand_2_total += 2
        elif i == "3":
            hand_2_total += 3
        elif i == "4":
            hand_2_total += 4
        elif i == "5":
            hand_2_total += 5
        elif i == "6":
            hand_2_total += 6
        elif i == "7":
            hand_2_total += 7
        elif i == "8":
            hand_2_total += 8
        elif i == "9":
            hand_2_total += 9
        elif i == "10":
            hand_2_total += 10

    
    for a in hand_2:
        if a == "A":
            if hand_2_total < 21 and (hand_2_total + 11) <= 21:
                hand_2_total += 11
            else:
                hand_2_total += 1
        else:
            continue
    
        
    
    if hand_1_total > 21 and hand_2_total > 21:
        return False
    if hand_1_total > 21:
        hand_1_total = 0
    if hand_2_total > 21:
        hand_2_total = 0
    
    return hand_1_total > hand_2_total