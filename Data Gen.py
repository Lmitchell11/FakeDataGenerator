#Liam Mitchell
#Fake sample Data Generator
import random
import statistics

ocs = []
while True:
  inStr = input(f"Enter Occurrence[{len(ocs)}]")
  if inStr:
    ocs.append(float(inStr))
  else:
    break
    
print(f"Occurrences: {ocs}")

if (len(ocs) < 1):
    exit()
mean = sum(ocs) / len(ocs)
print(f"Mean: {mean}")

if (len(ocs) < 2):
    exit()
stdDev = statistics.stdev(ocs)
print(f"Std Dev: {stdDev}")

for i, oc in enumerate(ocs):
    for j in range(1, 5):
        localMin = mean + 2*j*stdDev
        localMax = mean - j*stdDev
        if (oc >= localMax or oc <= localMin):
            ocs[i] = random.uniform(localMin, localMax)
            ocs[i] = "%.2f" % ocs[i]
            break

print(ocs)
