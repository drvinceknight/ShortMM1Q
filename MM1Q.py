# Shortest possible simulation of an MM1 Q (with warmup). Contributors: Geraint, Jason, Vince, Harald and Chris.
from random import expovariate
lmbda, mu, T, warmup, waits, sample, arrival_time, start_time, end_time = 1, 2, 5000, 1000, [], lambda x: expovariate(x), 0, 0, 0
while end_time < T:
    arrival_time += sample(lmbda)
    start_time = max(end_time, arrival_time)
    end_time = start_time + sample(mu)
    if arrival_time > warmup: waits.append(start_time - arrival_time)
print 'Mean wait: ' + str(sum(waits) / len(waits))
