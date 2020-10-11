
# Game of Maximization #


There are n piles of stones, where the i<sup>th</sup> pile has a<sub>i</sub> stones. You need to collect the maximum number of stones from these piles, but you must fulfill the following condition:

Let's say you pick x<sub>i</sub> (1<=i<=n) stones from the i<sup>th</sup> pile, then

* x<sub>1</sub> + x<sub>3</sub> + x<sub>5</sub> + ... = x<sub>2</sub> + x<sub>4</sub> + x<sub>6</sub> + ...
* 0 <= x<sub>i</sub> <= a<sub>i</sub>

For example, if  and n = 3 and a = [2,3,2], you can pick the stones as x = [1,2,1] becuase x<sub>1</sub> + x<sub>3</sub> = 1 + 1 = 2 and x<sub>2</sub> = 2

Find the maximum total number of stones you can pick.

__Input Format__:

The first line of input contains a single integer n denoting the number of piles.

The second line of input contains n space separated integers a<sub>i</sub>, where the i<sup>th</sup> integer denoted the number of stones in i<sup>th</sup> pile.

__Constraints__:

* 2 <= n <= 10<sup>5</sup>
* 1 <= a<sub>i</sub> <= 10<sup>3</sup>

__Output Format__:

Print a single integer denoting the maximum total number of stones you can pick.

__Sample Input 0__:

    4
    5  1  1  4
    
__Sample Output 0__:
  
    10
    
__Explanation 0__:

Let x = [4,1,1,4]. hence x<sub>1</sub> + x<sub>3</sub> = x<sub>2</sub> + x<sub>4</sub> and total number of stones picked is 10. It can be checked that its not possible to pick any greater number of stones.
    
__Sample Input 1__:

    3
    2  1  2
    
__Sample Output 1__:

    2
    
__Explanation 1__:

Let x = [0,1,1]. Hence x<sub>1</sub> + x<sub>3</sub> = x<sub>2</sub>, and the total number of stones picked is 2.
    
