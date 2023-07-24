#
"""
get birth_month
while birth_month < 1 or birth_month > 12
  display error message
  get birth_month
for count from 1 to birth_month
  display count
if birth month <= 6
  display First half
else
  display Second Half
"""
MINIMUM_MONTH = 1
MIDDLE_MONTH = 6
MAXIMUM_MONTH = 12
birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
while birth_month < MINIMUM_MONTH or birth_month > MAXIMUM_MONTH:
    print("Invalid month")
    birth_month = int(input(f"Enter the month number ({MINIMUM_MONTH}-{MAXIMUM_MONTH}): "))
for count in range(MINIMUM_MONTH, birth_month +1):
    print(count ,end=" ")
print()
if birth_month <= MIDDLE_MONTH:
    print("First half")
else:
    print("Second half")








