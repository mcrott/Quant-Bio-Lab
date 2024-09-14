library(tidyverse)
samp_starts <- readr::read_tsv("~/Quant Bio Lab/sample_coverage.csv")
samp_pdf <- readr::read_tsv("Quant Bio Lab/pdf_csv.csv")
samp_pois <- readr::read_tsv("Quant Bio Lab/pois_csv.csv")




colnames(samp_starts) <- c("name")
colnames(samp_pdf) <- c('pdf')
colnames(samp_pois) <- c('pois')


data_normal <- rnorm(n=1000000, mean=3, sd=sqrt(3))


colors = c("Simulated Coverages" = 'red',"Coverages PDF" = 'blue', "Coverages PMF" = 'green',
           "Normal Distribution" = 'orange')
ggplot(data=samp_starts,color = group) +
  geom_density(mapping=aes(x = samp_starts$name,color='red')) +
  geom_density(data = samp_pdf, mapping=aes(x=samp_pdf$pdf),color='blue') +
  geom_density(data=samp_pois,mapping=aes(x=samp_pois$pois),color='green') +
  geom_density(mapping=aes(x=data_normal),color='orange') +
  labs(x = "Coverage", y = "Frequency", title = "Coverage Plot with Overlays", 
       color = "Legend") +
  scale_color_manual(colors)+
  theme_minimal()

