l=[int(input())]
r=[]
while l:
    r.append(l.pop())
print(r)
''''The code you provided reverses the list l by repeatedly popping elements from the end of l and appending them to the list r. Here's how the code works step-by-step:

l = [8, 5, 3] initializes the list l.

r = [] initializes the empty list r.

The while l: loop continues as long as l is not empty.

The first iteration pops 3 from l and appends it to r, so l becomes [8, 5] and r becomes [3].
The second iteration pops 5 from l and appends it to r, so l becomes [8] and r becomes [3, 5].
The third iteration pops 8 from l and appends it to r, so l becomes [] (empty) and r becomes [3, 5, 8].
The while loop ends since l is now empty.

Finally, the code prints the reversed list r, which is:

csharp
Copy code
[3, 5, 8]


'''