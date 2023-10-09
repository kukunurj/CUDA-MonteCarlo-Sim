import matplotlib.pyplot as plt

# Data
data = [
    (1024, 32, 8.4589, 73.14),
    (1024, 64, 9.4451, 76.37),
    (1024, 128, 9.409, 74.12),
    (4096, 8, 49.8637, 74.76),
    (4096, 32, 52.0114, 74.66),
    (4096, 64, 38.659, 74.61),
    (4096, 128, 28.907, 74.93),
    (16384, 8, 121.9048, 74.83),
    (16384, 32, 123.1361, 75.1),
    (16384, 64, 203.094, 74.32),
    (16384, 128, 154.2169, 74.55),
    (65536, 8, 336.5653, 74.31),
    (65536, 32, 638.8023, 74.58),
    (65536, 64, 542.8041, 74.57),
    (65536, 128, 490.3041, 74.7),
    (262144, 8, 592.1214, 74.58),
    (262144, 32, 1539.8496, 74.6),
    (262144, 64, 1878.4683, 74.59),
    (262144, 128, 1773.5441, 74.72),
    (1048576, 8, 776.5297, 74.69),
    (1048576, 32, 2191.2532, 74.77),
    (1048576, 64, 2777.4199, 74.71),
    (1048576, 128, 3350.5113, 74.77),
    (2097152, 8, 807.2427, 74.67),
    (2097152, 32, 2674.7204, 74.67),
    (2097152, 64, 3986.8597, 74.69),
    (2097152, 128, 4347.6185, 74.68)
]

# Graph 1: Performance vs. NUMTRIALS with multiple curves of BLOCKSIZE
blocksize_values = [8, 32, 64, 128]
performance_data = [[] for _ in range(len(blocksize_values))]

for d in data:
    numtrials, blocksize, performance, _ = d
    blocksize_index = blocksize_values.index(blocksize)
    performance_data[blocksize_index].append((numtrials, performance))

plt.figure(figsize=(10, 6))
for i, blocksize in enumerate(blocksize_values):
    x, y = zip(*performance_data[i])
    plt.plot(x, y, label=f'BLOCKSIZE = {blocksize}')

plt.xlabel('NUMTRIALS')
plt.ylabel('Performance')
plt.title('Performance vs. NUMTRIALS')
plt.legend()
plt.grid(True)
plt.show()

# Graph 2: Performance vs. BLOCKSIZE with multiple curves of NUMTRIALS
numtrials_values = sorted(list(set([d[0] for d in data])))
performance_data = [[] for _ in range(len(numtrials_values))]

for d in data:
    numtrials, blocksize, performance, _ = d
    numtrials_index = numtrials_values.index(numtrials)
    performance_data[numtrials_index].append((blocksize, performance))

plt.figure(figsize=(10, 6))
for i, numtrials in enumerate(numtrials_values):
    x, y = zip(*performance_data[i])
    plt.plot(x, y, label=f'NUMTRIALS = {numtrials}')

plt.xlabel('BLOCKSIZE')
plt.ylabel('Performance')
plt.title('Performance vs. BLOCKSIZE')
plt.legend()
plt.grid(True)
plt.show()
