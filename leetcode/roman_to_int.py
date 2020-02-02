def romanToInt(s: str) -> int:
    sum = 0
    l = list(s)
    for i in range(0, len(l) - 1):
      if (l[i] + l[i+1] == "CM"):
        sum += 900
        i += 1
      else if (l[i] + l[i+1] == "XC"):
        sum += 90
        i += 1
      else if (l[i] + l[i+1] == "IX"):
        sum += 9
        i += 1
      else if (l[i] + l[i+1] == "IV"):
        sum += 4
        i += 1
      else if (l[i] == "M"):
        sum += 1000
      else if (l[i] == "C"):
        sum += 100
      else if (l[i) == "D"):
        sum += 500
      else if (l[i] == "L"):
        sum += 50
      else if (l[i] == "X"):
        sum += 10
      else if (l[i] == "V"):
        sum += 5
      else if (l[i] == "I"):
        sum += 1

    return sum

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV))




