"""Question: Angry Professor

A professor decides to cancel class if fewer than a certain number of students are present on time. Write a program to determine if the class is canceled.

Input:
- An integer `k` representing the threshold number of students.
- A list `a` of integers representing the arrival times of students (<= 0 means on time).

Output:
- "YES" if the class is canceled, "NO" otherwise.

Example:
Input: k = 3, a = [-1, -3, 4, 2]
Output: YES
Explanation:
Only 2 students are on time, which is less than the threshold of 3. Hence, the class is canceled.

A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, he decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time () to arrived late ().

Given the arrival time of each student and a threshhold number of attendees, determine if the class is canceled.

Input Format

The first line of input contains , the number of test cases.

Each test case consists of two lines.

The first line has two space-separated integers,  and , the number of students (size of ) and the cancellation threshold. 
The second line contains  space-separated integers () describing the arrival times for each student.

Note: Non-positive arrival times () indicate the student arrived early or on time; positive arrival times () indicate the student arrived  minutes late.

For example, there are  students who arrive at times . Four are there on time, and two arrive late. If there must be  for class to go on, in this case the class will continue. If there must be , then class is cancelled.

Function Description

Complete the angryProfessor function in the editor below. It must return YES if class is cancelled, or NO otherwise.

angryProfessor has the following parameter(s):

k: the threshold number of students
a: an array of integers representing arrival times
Constraints

Output Format

For each test case, print the word YES if the class is canceled or NO if it is not.

Note 
If a student arrives exactly on time , the student is considered to have entered before the class started.

Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1
Sample Output

YES
NO    """
def angryProfessor(k, a):
    count = 0
    for i in range(len(a)):
        if(a[i]<=0):
            count+=1
    if(count>=k):
        return "NO"
    return "YES"
