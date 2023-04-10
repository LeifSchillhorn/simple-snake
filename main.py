import snake

snak = snake.Snake()

snak.printState()
direction = ['e','s','w','s']
for direct in direction:
    print(f'Moving {direct}')
    snak.step(direct)

    snak.printState()
