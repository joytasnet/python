scores = {'network':60,'database':80,'security':50}
print(scores)
print(scores['network']) # 60
scores['programming'] = 65
scores['security'] = 55
print(scores)
del scores['security']
print(scores)
print(sum(scores.values()));

ls = [1,2,3]
del ls[1]
print(ls)
