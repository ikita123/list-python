element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even_count=0
odd_count=0
while i<len(element):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
    i=i+1
print("even number",even_count)
print("odd number",odd_count)