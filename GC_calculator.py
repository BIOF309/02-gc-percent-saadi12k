
# HW: Calculate a GC percentage

# first: define a string
flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'
print('The sequence is as follows : '+flu_ns1_seq)
print("The total numbers of G's, C's, and G's+C's in the sequence are, respectively:")
#use the count command to count specific letters
G=flu_ns1_seq.count('G')
C=flu_ns1_seq.count('C')
#add different variables to get a sum
GC=G+C
print("G's =" +str(G) + " , C's =" +str(C) + " , and G's+C's =" +str(GC) + ".")
ATCG= GC+flu_ns1_seq.count('A')+flu_ns1_seq.count('T')
print("The total number of nucletides in the sequence is " + str(ATCG))
GC_percent=(GC/ATCG)*100
print("The GC percent of the sequence is "+str(GC_percent))
