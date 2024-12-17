a=['a','b','c','a','c']
new=[]
for i in a:
    if i not in new:
        new.append(i)
print(new)
""""
Line-by-Line Explanation:
a = ['a', 'b', 'c', 'a', 'c']

This line creates a list called a that contains the elements ['a', 'b', 'c', 'a', 'c'].
This list has some duplicate elements ('a' and 'c' appear twice).
new = []

This line creates an empty list called new. We'll use this list to store the unique elements from the list a, keeping only the first occurrence of each element.
Initially, the new list is empty.
for i in a:

This line starts a for loop. It will go through each element in the list a one by one.
For example, i will first be 'a', then 'b', then 'c', then 'a', and finally 'c'.
if i not in new:

This line checks if the current element i (from the list a) is already in the new list.
The in operator checks whether i is already present in new.
The not operator means that the condition will only be True if i is not in the new list.
So, if i has not been added to new before, the condition will be True, and the code inside the if block will run.
new.append(i)

If the element i is not already in the new list, this line adds i to the new list.
The append() function adds the element to the end of the list.
This ensures that only the first occurrence of each element is added to new.
print(new)

After the loop finishes (i.e., after checking all elements in the list a), this line prints the final new list.
The new list now contains only the unique elements from a, in the same order they first appeared in a.
Example Walkthrough:
Let's go through the loop step by step:

Initially, new = [].
The loop starts with the first element in a, which is 'a'.
'a' is not in new, so it's added to new. Now, new = ['a'].
Next, the loop moves to the second element, which is 'b'.
'b' is not in new, so it's added to new. Now, new = ['a', 'b'].
Then, the loop moves to the third element, which is 'c'.
'c' is not in new, so it's added to new. Now, new = ['a', 'b', 'c'].
Now, the loop reaches the fourth element, which is 'a' again.
'a' is already in new, so it is not added again. The if condition is False, and the loop moves on to the next element.
Finally, the loop reaches the fifth element, which is 'c' again.
'c' is already in new, so it is not added again. The loop ends.
Final Output:
After the loop finishes, the list new contains ['a', 'b', 'c']. This list is then printed, which results in the output:

css
Copy code
output:
['a', 'b', 'c']
Summary:
The code goes through each element of the list a.
It checks if that element has already been added to the new list.
If not, it adds it to new.
The result is that new contains only the first occurrence of each element from a, without duplicates.
This way, duplicates in the original list a are removed, and the order of the first occurrences is preserved.




"""