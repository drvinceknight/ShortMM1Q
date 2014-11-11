# Shortest possible simulation of an MM1 Q
from random import expovariate
lmbda = 1
mu = 2
T = 500
sample = lambda x: expovariate(x)
arrival_time = sample(lmbda)
start_time = arrival_time
end_time = arrival_time + sample(mu)
waits = []

while end_time > T:
    arrival_time += sample(lmbda)
    start_time = max(end_time, arrival_time)
    end_time = start_time + sample(mu)
    waits.append(end_time - start_time)
print waits
