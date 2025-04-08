# Statistics Module
import statistics as stats
import math as m

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]
print(sorted(agesData), '\n')

print(stats.mean(agesData))
print(stats.mode(agesData))
print(stats.median(agesData), '\n')

print(stats.variance(agesData))
print(stats.stdev(agesData))
print(m.sqrt(stats.variance(agesData)))
