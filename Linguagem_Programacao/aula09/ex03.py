n = [10,9,6,4,2]

print(n[0])
som = 0
sub = 0
for i in range(len(n)):
    if(i % 2 != 0):
        som += n[i]
    else:
        if(i == 2):
            sub += n[i]
        else:
            sub -= n[i]
    
print(som)
print(sub)