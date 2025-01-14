def count11(seq):
   # define this function and return the number of occurrences as a number
   amount = 0
   for i in range(0, len(seq) -1):
         if seq[i] == 1 and seq[i+1] == 1:
              amount += 1
      
   return amount

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2
