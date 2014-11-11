# Shortest possible simulation of an MM1 Q
from random import expovariate
lmbda, mu, T, warmup, waits, sample = 1, 2, 5000, 1000, [], lambda x: expovariate(x)
arrival_time = sample(lmbda)
start_time, end_time = arrival_time, arrival_time + sample(mu)

while end_time < T:
    arrival_time += sample(lmbda)
    start_time = max(end_time, arrival_time)
    end_time = start_time + sample(mu)
    if arrival_time > warmup:
        waits.append(start_time - arrival_time)
print sum(waits) / len(waits)
