library(tidyverse)
samp_starts <- readr::read_tsv("~/Quant Bio Lab/sample_coverage.tsv")






myls <- seq(nrow(samp_starts))



data_normal <- dnorm(myls, mean=3, sd=sqrt(3))*1000000




ggplot(data=samp_starts) +
  geom_line(mapping=aes(x=cnts,y=coverage,color='red')) +
  geom_line(mapping=aes(x=cnts,y=pmf,color='blue')) +
  geom_line(mapping=aes(x=cnts,y=pdf,color='green')) +
  theme_classic()

