# import packages
library('ini')
library('mongolite')
library('rjson')

# get mongo ip address from mongo.ini
filepath <- '/Users/fofx/dss15/crawling_project/daangn/mongo.ini'
data <- read.ini(filepath, encoding = getOption("encoding"))


# get collection data from mongodb
db <- mongo(
        collection = "D20120700", 
        db = "daangn",
        url = data$mongo$ip_address, 
        verbose = TRUE
) 

# import collection into df
df <- db$find('{}')
head(df)

# drop current collection
db$drop()

# change lat, lon into numeric data
df$lat <- as.numeric(df$lat)
df$lon <- as.numeric(df$lon)
# drop na
df <- na.omit(df)

# jitter geocode so that there won't be any duplicates
df$lat <- jitter(df$lat)
df$lon <- jitter(df$lon)

# put it back to mongodb
db$insert(df)