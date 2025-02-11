"""
Given an array of positive integers representing the values of coins in your possession,
write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create.
The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4.
If you're given no coins, the minimum amount of change that you can't create is 1.

Test 1:{
  "coins": [5, 7, 1, 1, 2, 3, 22]
}
output: 20

Test 2: {
  "coins": [1, 1, 1, 1, 1]
}
Output: 6

Test 3: {
  "coins": [1, 5, 1, 1, 1, 10, 15, 20, 100]
}
Output: 55

Test 4: {
  "coins": [6, 4, 5, 1, 1, 8, 9]
}

Expected Output: 3

Test 5: {
  "coins": []
}
Expected Output: 1

Test 6: {
  "coins": [87]
}

Expected Output: 1

Test 7: {
  "coins": [5, 6, 1, 1, 2, 3, 4, 9]
}
Expected Output: 32

Test 8: {
  "coins": [5, 6, 1, 1, 2, 3, 43]
}
Expected Output: 19

Test 9: {
  "coins": [1, 1]
}
Expected Output: 3

Test 10: {
  "coins": [2]
}
Expected Output: 1

Test 11:
{
  "coins": [1]
}
Expected Output: 2

Test 12: 
{
  "coins": [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]
}
Expected Output: 87

Test 13: {
  "coins": [1, 2, 3, 4, 5, 6, 7]
}
Expected Output 29
"""

def nonConstructibleChange(coins):
    coins.sort()  # Sort the coins
    current_change_created = 0

    for coin in coins:
        # If the next coin is greater than the smallest amount of change we can't create + 1
        if coin > current_change_created + 1:
            return current_change_created + 1
        current_change_created += coin

    # If all changes can be created, return current_change_created + 1
    return current_change_created + 1