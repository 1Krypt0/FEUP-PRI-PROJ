
# library
library(wordcloud2)

file <- "data/spacenews_filled.csv"
data <- read.csv(file)

# Number of news published each year
data_publishing_year <- as.numeric(format(
    as.Date(data$date, "%B %d, %Y"), "%Y"
))
hist(data_publishing_year,
    breaks = 20, xlab = "Year", xlim = c(2005, 2025),
    main = "Histogram of news' year of publishing"
)


# Frequency of authors (at least 100 articles)
table_authors <- table(data$author)
frequent_authors <- data[
    data$author %in% names(table_authors[table_authors > 100]),
]
barplot(sort(table(frequent_authors$author), decreasing = TRUE),
    las = 2, cex.names = 0.6,
    main = "Frequency of articles by authors with at least 100 articles"
)
