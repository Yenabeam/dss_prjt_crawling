# import packages
library('ini')
library('mongolite')
library('rjson')

# get mongo ip address from mongo.ini
filepath <- '/home/ubuntu/python3/projects/daangn/mongo.ini' # insert your mongo.ini path
#filepath <- '/Users/fofx/dss15/crawling_project/daangn/mongo.ini'
data <- read.ini(filepath, encoding = getOption("encoding"))

# get current time
current_time <- Sys.time()
# change format
my_collection <- paste('D',toString(format(current_time, format = '%y%m%d%H', mark=TRUE)), sep='')


# get collection data from mongodb
db <- mongo(
        collection = my_collection, 
        db = "daangn", # change to "joongo" when needed
        url = data$mongo$ip_address, 
        verbose = TRUE
) 

# import collection into df
df <- db$find('{}')
head(df)

# drop current collection
db$drop()

# drop na
df <- na.omit(df)

# change lat, lon into numeric data
df$lat <- as.numeric(df$lat)
df$lon <- as.numeric(df$lon)

# jitter geocode so that there won't be any duplicates
df$lat <- jitter(df$lat)
df$lon <- jitter(df$lon)

# put it back to mongodb
db$insert(df)
