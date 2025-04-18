stmt="Good morning aravind"
word=stmt.split(" ")
d={}
for i in range(len(word)):
    count=len(word[i])
    d[word[i]]=count
print(d)
    
