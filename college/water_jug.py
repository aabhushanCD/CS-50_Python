def jug(jug_A,jug_B, goal):
    jug_A=0
    jug_B=0

    while jug_A != goal and jug_B != goal:
        if jug_A == 0:
            jug_A = 3
        elif jug_B == 5:
            jug_B = 0
        elif jug_A > 0 and jug_B !=5:
            a = min(jug_A , 5 - jug_B)
            jug_A -= a
            
            jug_B = a + jug_B
        else:
            pass
    return jug_A,jug_B
goal = 4
result = jug(3, 5, goal)
print("Jug A:", result[0])
print("Jug B:", result[1])