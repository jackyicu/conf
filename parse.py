with open('ads.txt', 'w') as f:
    for line in f:
        line += ',REJECT'
        f.write(line)
        