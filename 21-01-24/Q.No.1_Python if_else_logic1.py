# A single line containing a positive integer, .

# Constraints
# 1<=n<=100
# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Explanation 0
# n=33
# nis odd and odd numbers are weird, so print Weird

logic 1

n = int(input().strip())
if n % 2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
