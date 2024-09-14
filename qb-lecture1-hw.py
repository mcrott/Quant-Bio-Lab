#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# random_seed = 758223784


# np.random.seed(random_seed)

#num reads from 1.1 = 300000

#storing read locations
chrom = np.zeros(1000000, int)
start_pos = []
#random sample positions within the 1 mbp genome
#30000 is the number of reads for 3x coverage of a 1mbp genome
for i in range(30000):
    #generate uniform distribution then identify the genome start location
    start = np.random.randint(0,999900)
    start_pos.append(start)
    end = start + 100
    chrom[start:end] += 1

max_cov = max(chrom)
poisson = list(range(0,max_cov+1))

"""

num_reads = calculate_number_of_reads(genomesize, readlength, coverage)
​
## use an array to keep track of the coverage at each position in the genome
genome_coverage = initialize_array_with_zero(genomesize)
​
for i in range(len(num_reads)):

  startpos = uniform_random(0,genomelength-readlength+1)
  endpos = startpos + readlength
  genomecoverage[startpos:endpos] += 1

## get the range of coverages observed
maxcoverage = max(genomecoverage)​
xs = list(range(0, maxcoverage+1))

## Get the poisson pmf at each of these
poisson_estimates = get_poisson_estimates(xs, lambda = coverage)

## Get normal pdf at each of these (i.e. the density between each adjacent pair of points)
normal_estimates = get_normal_estimates(xs, mean = genome_coverage, stddev = sqrt(genome_coverage))
​
## now plot the histogram and probability distributions


"""

chrom1 = np.histogram(chrom,bins=max(chrom)+1)

pmf = stats.poisson.pmf(poisson,mu=3,loc=3)
pdf = stats.norm.pdf(poisson,loc=np.mean(poisson), scale=np.sqrt(np.mean(poisson)))

#scaling
pmf = pmf*1000000
pdf = pdf*1000000



df = pd.DataFrame(poisson,columns=['cnts'])


print(len(chrom1[0]))
print(len(pmf))
print(len(pdf))


df['coverage'] = chrom1[0]
df["pmf"] = pmf
df['pdf'] = pdf


df.to_csv('sample_coverage.tsv',sep="\t",index=False)
# df1.to_csv('pois_csv.csv',index=False)
# df2.to_csv('pdf_csv.csv',index=False)


"""

"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

"""
"""
"""
"""
