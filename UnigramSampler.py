import numpy as np

corpus = np.array([0,1,2,3,4,1,2,3])
power = 0.75
sampler = Unigramsampler(corpus, power, sample_size)
target = np.array([1,3,0])
negative_sample = sampler.get_negative_sample(target)
print(negative_sample)

