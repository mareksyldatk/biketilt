library(dplyr)
library(ggplot2)

d1 <- read.csv("20160716123101.csv")
d2 <- read.csv("20160716163834.csv")
d3 <- read.csv("20160716200736.csv")
df <- rbind.data.frame(d1, d2, d3)
df <- df[complete.cases(df),]

qplot(Longitude, Latitude, data=df, colour=Velocity) + scale_colour_gradient(low="white", high="blue") + coord_fixed(ratio = 1)
