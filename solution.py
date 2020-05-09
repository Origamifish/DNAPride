testCases = int(input())

for x in range(testCases):
  ans = ""
  length = int(input())
  seq = input()
  for x in range(length):
      b = seq[x]
      if b == 'A':
          ans += "T"
      elif b == 'T':
          ans += "A"
      elif b == 'C':
          ans += "G"
      elif b == 'G':
          ans +="C"
      else:
        ans = "Error RNA nucleobases found!"
        break                       
  print(ans)
