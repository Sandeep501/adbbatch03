name = "Chiranjeevi" # -- 5 vowels
vowels = ['a', 'e', 'i', 'o', 'u']

cnt = 0
for chrec in name:
    if chrec in vowels:
        cnt+=1   # -- cnt = cnt + 1 
print(cnt)