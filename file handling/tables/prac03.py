for i in range(2,6):
    with open(f'table_of_{i}.t','w') as f:
        for j in range (1,11):
            f.write(f'{i}X{j}={i*j}')
            if j!=10:
                f.write('\n')