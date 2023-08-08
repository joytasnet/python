for i in range(1,10):
    if i % 2 == 0:
        continue
    for j in range(1,10):
        if i*j >50:
            break
        print(f'{i*j}',end=' ')
    print()
