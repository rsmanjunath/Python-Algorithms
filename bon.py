"""
Question: Bon Appétit

Write a program to determine if the bill was split fairly between two friends. If not, calculate the amount one friend owes the other.

Input:
- A list `bill` of integers representing the cost of each item ordered.
- An integer `k` representing the index of the item Anna did not eat.
- An integer `b` representing the amount Anna contributed.

Output:
- "Bon Appetit" if the bill was split fairly, otherwise the amount Anna owes.

Example:
Input: bill = [3, 10, 2, 9], k = 1, b = 7
Output: "Bon Appetit"
Explanation:
Anna did not eat the item costing 10. The total cost of the remaining items is 3 + 2 + 9 = 14. Anna's share is 14 / 2 = 7, which matches her contribution.
"""

def bonAppetit(bill,k,b):
    del bill[k]
    share = sum(bill) // 2
    
    if share == b:
        return "Bon Appetit"
    else:
        return b - share

    
    


print(bonAppetit([3,10,2,9],1,7))