# CUDA: Monte Carlo Simulation

This project involves a Monte Carlo simulation implemented using CUDA, a parallel computing platform and application programming interface model created by NVIDIA. The simulation focuses on analyzing performance patterns and probabilities associated with varying block sizes and number of trials.

## Machine Specifications
- **Machine:** Nvidia DGX system

## Performance Results

The performance analysis revealed the following patterns:

1. Performance tends to increase as the number of trials (NUMTRIALS) increases.
2. Performance varies with the block size (BLOCKSIZE).
3. Optimal performance is achieved at certain combinations of NUMTRIALS and BLOCKSIZE.

These patterns are influenced by workload distribution, thread utilization, memory access patterns, and GPU architecture.


---

Please refer to the file CUDA_Simulation.pdf for thorough analysis.

