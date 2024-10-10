zipT, dokT = map(int, input().split())
walk, sleep = map(int, input().split())
Zip = zipT + ((zipT-1)//8) * sleep
Dok = walk + dokT + ((dokT-1)//8) * (2 * walk + sleep)

if Zip > Dok:
  print("Dok")
  print(Dok)
elif Zip < Dok:
  print("Zip")
  print(Zip)