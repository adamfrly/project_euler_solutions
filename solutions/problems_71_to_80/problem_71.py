# Find the proper fraction under 1 that would be directly to the left of 3/7 if the denominator could be any d < 1000000

# Done mostly by hand
# Find the highest number under 1,000,000 that divisible by both 3 and 7 (it's 999,999)
for i in range(1000000, 999000, -1):
    if i % 3 == 0 and i % 7 == 0:
        print(i)

# Find what the numerator would be if 3/7 were turned into a fraction with 999,999 as the denominator (428,571/999,999)
# Subtract one from the numerator and you have your answer

print(428570)