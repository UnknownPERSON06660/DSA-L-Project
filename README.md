# DSA-L-Project

Binary Search

Binary search is a fast way to find a number in a list. (The list must be sorted)
In the he following code we perform a binary search in a list, if the value is found it will return the value or else it will return –1.
Following is the breakdown of the code:

I.	In first step, we define the function named binary search. It takes 2 parameters as input arr(array) & t(target value).
II.	Then we initialize 2 variables l(left) and r(right) whose values are 0 and length of array, respectively.
III.	In third step, we created a while loop to search the value in the array. The loop will run until the value of l is smaller or equal to value of r.
IV.	In next step, we created a variable named mid which and the value equals to the middle of the list. We did this so we can easily divide the list into half.
V.	Then I use if condition to check if the number at the middle matches the target value or not. If the number matches the search will end here.
VI.	In next step I used a formula to adjust the value of search range. If the middle value is less than the target value, it means the target value is on the right part of the list, so we move to right. And if the middle value is greater than the target value, then it means that target must be in the left part of the list.
VII.	At the end of the function we return –1, it executes only if the while loop can’t find the value.
VIII.	At the end of the program, I initialize a list in n variable and the target value in t variable. After that I call the function by passing the n and t variable in it. And then it will check if the returned value is not equals to –1 it will tell the index of the value or else it will say value not found.


Linear Search

Linear search is a simple method to find a number in a list.
In the following code, we perform a linear search in a list. If the value is found, it will return the index of the value; otherwise, it will return -1.

Following is the breakdown of the code:
I. In the first step, we define a function named linear_search. It takes two parameters as input: arr (the array) and t (the target value).
II. Inside the function, we use a for loop to go through each element in the list one by one.
The enumerate function is used to get both the index (i) and the value (v) of each element in the list.
III. For each element in the list, we use an if condition to check if the current value (v) matches the target value (t).
    If the value matches, the function immediately returns the index (i) where the target value is found.
IV. If the loop completes without finding the target value, the function returns -1.
This indicates that the target value is not in the array.
V. At the end of the program, we initialize a list in the n variable and the target value in the t variable.
We then call the linear_search function by passing n and t as arguments.
The result is stored in the variable r.
    If r is not -1, it means the target value is found, and we print its index.
    Otherwise, we print "Target not found."
