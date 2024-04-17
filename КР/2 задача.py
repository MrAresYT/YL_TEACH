def goal(*ls, life=7):
    dc = {}
    for i, word in ls:
        i //= life
        if i in dc.keys():
            dc[i].append(word)
        else:
            dc[i] = [word]
    for k in dc.keys():
        dc[k] = sorted(dc[k])
    return dc


lines = [
    (3, 'room'), (12, 'village'), (48, 'wardrobe'),
    (13, 'clothes'), (4, 'window'), (1, 'nature'),
    (14, 'Lake'), (5, 'forest')
]
print(goal(*lines, life=3))
