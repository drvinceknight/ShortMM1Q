#Shortest possible simulation of an MM1 Q
import random
lmbda        = 1
mu           = 2
T            = 500
sample       = lambda x: random.expovariate(x)
t            = 0
arrival_time = t + sample(lmbda)
start_time   = arrival_time
end_time     = sample(mu)
waits        = []

while end_time < T:
    arrival_time  += sample(lmbda)
    start_time     = max(end_time,arrival_time)
    end_time       = start_time + sample(mu)
    waits.append(end_time - start_time)
print waits
