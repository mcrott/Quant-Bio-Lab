
## 1.1
How many 100bp reads are needed to sequence a 1Mbp genome to 3x coverage?


> 3*1Mbp = 3Mbp/100bp-read = 30k reads


## 1.4

5.1% of the genome has not been sequenced

The poisson distribution  is shifted to the right in comparison to the genome coverage data from 30000 reads. 

## 1.5

0.0031000000000000003 % of the genome has been sequenced with 0 reads. 
Poisson distribution is pretty much the same as 1.4. Its shifted to the right in comparison to the coverage data from 100000 reads. 

## 1.6
0.0006000000000000001 % of the genome has been sequenced with 0 reads. 

## 2.1
Duplicate edges are present, total was 14 uniques

## 2.4
See python script

## 2.5
ATT
 ||
 TTC
  ||
  TCT
   ||
   CTT
    ||
    TTA
attctta

## 2.6
Rough question. First you would need sufficient coverage of the genome, ie 30-40x. Secondly, you would need a fantastic algorithm to search for kmers. We only used k=3, but id suspect you would want upwards to k=500 to 1000 for accurate coverage. 

