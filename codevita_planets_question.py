'''Codu lives in a solar system consisting of three planets. These planets revolve around their sun in a circular path. 

In that solar system, all the three planets have a common time measure called a "click" and a distance measure "dist". The planets revolve in an anti-clockwise direction with angular velocity V1, V2, and V3 degrees/click respectively. The radii of the circular paths are R1, R2, and R3 dists respectively. Initially, all planets start from position (given in figure) S1, S2, and S3 respectively. Codu wants to know if they would be aligned in a straight line after a time period of N clicks.

 

Constraints:

0 <= R <= 10^8
0 <= V <= 10^8
0 <= N <= 10^8
1 <= T <= 10
 
Input:

The input consists of multiple test cases in the same line, and each test case must have an output in the output file.
The first line consists of integer T denoting the number of test cases.
This is followed by a set of three lines of each of the T test cases.
The first line of each test case consists of three separated integers R1, R2, R3 denoting the radius of the circular paths dists.
The second line of each test case contains space separated integers V1, V2, V3 denoting the angular velocity of the planets in degrees/clicks.
The third line of each test case contains time N(in clicks) after which the condition of alignment of the planets in a straight line is to be checked.
 
Output:

Print TRUE if all of them are aligned in a straight line after N click, else print FALSE.
 

Time Limit:

1 sec

 

Test Case:

2

10 7 30

5 15 36

12

5 10 15

1 2 4

360

 

Output:

FALSE
TRUE

 

Explanation:

There are 2 test cases.
The first test case gives R1=10, R2=7, R3=30. It also gives V1=5, V2=15, V3=36. N is given as 36 clicks.
Here, none of the planets will be aligned in a straight line. Hence the output is FALSE.

The second test case gives R1=5, R2=10, R3=15. It also gives V1=1, V2=2, V3=4. N is given as 360 clicks.
Here, all the planets will be at location R1, R2 and R3 respectively after completing the 360 clicks. and hence will be aligned. The output is TRUE.
Specifically, planet 1 will complete one revolution, planet 2 will complete two revolutions, and planet 3 will complete four revolutions around the sun.'''