library(dplyr)
library(ggplot2)
library(RgoogleMaps)
library(png)
library(grid)
library(rgdal)

preprocess.csvA <- function(filename) {
  head(read.csv(filename), -6) %>% mutate(Speed=Velocity) %>% select(Latitude, Longitude, Speed)
}
preprocess.csvB <- function(filename) {
  read.csv(filename) %>% mutate(Speed = Speed.m.s. * 3.6) %>% select(Latitude, Longitude, Speed)
}
preprocess.kml <- function(filename, layername) {
  coordinates(readOGR(dsn=filename, layer=layername)) %>% data.frame %>% 
    rename(Latitude=X2, Longitude=X1) %>% mutate(Speed=66.8827)
}

# Load data
t01 <- preprocess.csvA("data/20160711181706.csv")
t02 <- preprocess.csvA("data/20160711193353.csv")
t03 <- preprocess.csvA("data/20160715194016.csv")
t04 <- preprocess.csvA("data/20160716123101.csv")
t05 <- preprocess.csvA("data/20160716163834.csv")
t06 <- preprocess.csvA("data/20160716200736.csv")
t07 <- preprocess.csvA("data/20160718175539.csv")
t08 <- preprocess.csvA("data/20160721194729.csv")
t09 <- preprocess.csvA("data/20160724120814.csv")
t10 <- preprocess.csvA("data/20160724174918.csv")

t11 <- preprocess.kml("data/20160729000000.kml", "Kawno-Miedzyzdroje")

t13 <- preprocess.csvB("data/20160730_Polnocne_Niemcy.csv")
t14 <- preprocess.csvB("data/20160812_Lazy.csv")
t15 <- preprocess.csvB("data/20160813_Ustka.csv")
t16 <- preprocess.csvB("data/20160815_Bobiecino.csv")
t17 <- preprocess.csvB("data/20160816_Wierzchowo.csv")

# Combine and clean data
df <- rbind.data.frame(t01, t02, t03, t04, t05, t06, t07, t08, t09, t10, t11, t13, t14, t15, t16, t17)
df <- df[complete.cases(df),]
df$Average.Speed <- SMA(df$Speed, 50)

# 
# Plot
#

# loading the required packages
library(ggplot2)
library(ggmap)

# creating a sample data.frame with your lat/lon points
lon <- c(13.0, 18.0)
lat <- c(53.5, 54.5)

# getting the map
mapgilbert <- get_map(location = c(lon = mean(lon), lat = mean(lat)), zoom = 7, maptype = "toner-lite", scale = 1)

# plotting the map with some points on it
ggmap(mapgilbert, xlim=lon, ylim=lat) +
  geom_point(data = df, aes(x = Longitude, y = Latitude, col=Average.Speed), size = I(1.0), shape = 21, alpha=0.9) +
  # scale_colour_gradientn(colours = topo.colors(10)) +
  scale_colour_gradient(low = "orange", high = "blue") +
  guides(fill=FALSE, alpha=FALSE, size=FALSE) +
  labs(x="Longitude", y="Latitude") +
  ggtitle("Moto Summer 2016 #latoFazera ")
