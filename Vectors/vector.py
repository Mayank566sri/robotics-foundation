v1 = []
i=0
while i<3:
    v1.append(int(input(f"enter the {i+1} element of v1:- ")))
    i+=1
    
v2 = []
i=0
while i<3:
    v2.append(int(input(f"enter the {i+1} element of v2:- ")))
    i+=1
    
vector_sum = []
i=0
for i in range(len(v1)):
    vector_sum.append(v1[i] + v2[i])
    i+=1
    
dot_product = 0
i=0
for i in range(len(v1)):
    dot_product += v1[i]*v2[i]
    i+=1
    
print("First vector :- ", v1)    
print("Second vector :- ", v2)    
print("Vector addition :- ", vector_sum)
print("Dot product :- ", dot_product)