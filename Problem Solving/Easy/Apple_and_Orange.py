def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0
    
    for apple in apples:
        if s <= (a + apple) <= t:
            apples_on_house += 1
            
    for orange in oranges:
        if s <= (b + orange) <= t:
            oranges_on_house += 1
            
    print(apples_on_house)
    print(oranges_on_house)
