ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
summa = ""
STO = "hundred"
TYSHA = "thousand"
for i in range(1, 10):
        if (i == 1):
            for g in range(1, 20):
                summa += ONES[g]
        if (i > 1):
            for g in range(0, 10):
                summa += TENS[i] + ONES[g]
for i in range(1, 10):
    summa += ONES[i] + STO
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


