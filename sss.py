with open("sd.txt","r") as f:
    data =  f.read()

lines = data.split("\n")

print(lines)
result=[]
word="gvxn"
for y in range(len(lines)):
    for x in range(len(lines[y])):
        s=lines[y][x]
        if s==word[0]:
            check=True
            if x+len(word)-1<len(lines[y]):
                for i in range(len(word)):
                    if lines[y][x+i]!=word[i]:
                        check=False
                        break
                if check:
                       result.append([x+1],[y+1])
            check=True
            if x-len(word)+1>=0:
                for i in range(len(word)):
                    if lines[y][x-i]!=word[i]:
                        check=False
                        break
                if check:
                    result.append([x+1,y+1])
print(result)
