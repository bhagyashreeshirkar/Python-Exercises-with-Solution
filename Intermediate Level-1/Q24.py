"""
Write a program to display following output.

Input format: Input consists of 4 integers.
The first input corresponds to the total number of balls.
The second input corresponds to the total number of runs.
The third input corresponds to the total number of runs scored.
The forth input corresponds to the number of balls bowled.

Output format:
The first output corresponds to the total number of overs.
The second output corresponds to the total number of overs finished.
The third output corresponds to the current run rate.
The forth output corresponds to the total run rate.

Example:
Input:
300
375
78
45
Output:
Total no of overs: 50
No of overs finished: 7.3
Current run rate: 10.7
Total run rate: 7.5

Explanation:
Here in input, they have given the number of balls is 300 with this find the number of overs
 (since 6 balls = 1 over, 300 balls = 300/6 overs = 50 overs), so first output will be 50.

Out forth input is the total number of balls bowled with this find the total number of overs finished
(45 balls bowled, so no of overs finished = 7.3), hence the second output is 7.3

So current run rate can be calculated by current score/no of overs finished = 78/7.3, hence the third output is 10.7

For total run rate = total score/total no of overs = 375/50 = 7.5
"""

total_no_of_balls = int(input())
total_score = int(input())
current_score = int(input())
no_of_balls_bowled = int(input())


total_overs = total_no_of_balls/6
print('Total no of overs:', round(total_overs))

a = no_of_balls_bowled // 6
b = no_of_balls_bowled % 6
no_of_overs_finished = f'{a}.{b}'
print(f'No of overs finished: {no_of_overs_finished}')

current_run_rate = current_score/float(no_of_overs_finished)
print('Current run rate:', round(current_run_rate, 1))

print('Total run rate:', total_score/total_overs)
