ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
summa = ""
STO = "hundred"
TYSHA = "thousand"
for i in range(1, 10):
        if (i == 1):
            for g in range(1, 20):
                summa += TENS[i] + ONES[g]
        if (i > 1):
            for g in range(0, 10):
                summa += TENS[i] + ONES[g]
summa += ONES[1] + STO
for i in range(1, 10):
    for t in range(1, 10):
        if (t == 1):
            for g in range(1, 20):
                summa += ONES[i] + STO + "and" + TENS[t] + ONES[g]
        else:
            for g in range(0, 10):
                summa += ONES[i] + STO + "and" + TENS[t] + ONES[g]
summa += ONES[1] + TYSHA
print(len(summa))

# def compute():
#     ans = sum(len(to_english(i)) for i in range(1, 1001))
#     return str(ans)
#
#
# def to_english(n):
#     if 0 <= n < 20:
#         print(ONES[n])
#         return ONES[n]
#     elif 20 <= n < 100:
#         print(TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else ""))
#         return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
#     elif 100 <= n < 1000:
#         print(ONES[n // 100] + "hundred" + (("and" + to_english(n % 100)) if (n % 100 != 0) else ""))
#         return ONES[n // 100] + "hundred" + (("and" + to_english(n % 100)) if (n % 100 != 0) else "")
#     elif 1000 <= n < 1000000:
#         print(to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n % 1000 != 0) else ""))
#         return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n % 1000 != 0) else "")
#     else:
#         raise ValueError()
#
#
# ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
#         "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
# TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
#
#
# if __name__ == "__main__":
#     print(compute())