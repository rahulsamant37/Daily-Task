"""
Consider that we have few elements to be inserted into the priory queue. Elements inserted into the queue are in the following format (x, y) where x is the element and y 
is its priority. Element with high y value indicates high priority. If two elements having the same priority element with smaller x value will get high priority. K is the 
number of elements that have to be removed from the queue that has the highest priority and displays the elements that are not removed from the queue as per the priority. 
(from high priority to low priority elements) Read the input from STDIN and print the output to STDOUT. Do not write arbitrary strings while reading the input or while printing, 
as these contribute to the standard output.


Constraints:
1) x should be unique.
ii) x and y should not be negative.


Input Format:
The first line of input contains N, where N denotes the number of elements.
Next N lines of input contain x and y where x is the element and y is its priority.
The last line of input contains K where K denotes the number of elements to be deleted from the queue.
Output Format:
The output contains the elements that are not deleted from the queue based on their priority.

Sample Input1:
5
2 4
5 3
6 1
7 4
9 4
3
Sample Output1:
5 6
Explanation1:
From the given Sample Input1, we have:
Total number of elements= 5

Consider the table given below:

Priority | Elements order from left to right
---------|----------------------------------
4        |            2->7->9
3        |               5

Total number of elements to be deleted-3
So clearly 2, 7, and 9 are having the highest priority as 4 will get deleted.
The remaining elements are 5 and 6, which will be printed as an output.

"""

def process_data(n, k, x, y):
    # Create list of (element, priority) pairs
    elements = list(zip(x, y))
    
    # Sort by priority (descending) and then by element value (ascending)
    # Using negative priority for descending order, positive element for ascending
    elements.sort(key=lambda item: (-item[1], item[0]))
    
    # Remove first K elements (highest priority)
    remaining = elements[k:]
    
    # Output the remaining elements
    for element, priority in remaining:
        print(element, end=" ")

def main():
    n = int(input())
    x = []
    y = []
    
    for i in range(n):
        x_val, y_val = map(int, input().split())
        x.append(x_val)
        y.append(y_val)
    
    k = int(input())
    process_data(n, k, x, y)

if __name__ == "__main__":
    main()