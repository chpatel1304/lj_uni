#wap to create a list of words of string entered by user each word
#has first and last letter capital
s="abcd efgh pqr"
n_l=[]
l=s.split()
for i in l:
    n_l.append(i[0].upper()+i[1:-1:1]+i[-1].upper())
print(n_l)
#wap to make a list by running through elements of the list by adding all elements
#greater and its self
