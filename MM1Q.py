# Shortest possible simulation of an MM1 Q
from random import expovariate
lmbda, mu, T, waits, sample = 1, 2, 500, [], lambda x: expovariate(x)
arrival_time = sample(lmbda)
start_time = arrival_time
end_time = arrival_time + sample(mu)

while end_time < T:
    arrival_time += sample(lmbda)
    start_time = max(end_time, arrival_time)
    end_time = start_time + sample(mu)
    waits.append(end_time - arrival_time)
print waits