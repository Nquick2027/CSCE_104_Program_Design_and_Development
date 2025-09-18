print('twos\tthrees\tfours\tfives\tsixes\tsevens\teights\tnines\ttens')
for i in range(2, 11):
    one_line = ''
    for j in range(2, 11):
        mult = '{}x{}={}\t'.format(j, i, i*j)
        one_line += mult
    print(one_line)

