
file <- "data/spacenews_filled.csv"
data <- read.csv(file)
formated_date <- as.numeric(format(as.Date(data$date, "%B %d, %Y"), "%Y"))
hist(formated_date,
    breaks = 20, xlab = "Year", xlim = c(2005, 2022),
    main = "Year of publishing"
)
