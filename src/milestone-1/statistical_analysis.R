news_data <- read.csv("data/spacenews_final.csv")
authors_data <- read.csv("data/authors.csv")
tags_data <- read.csv("data/tags.csv")
sections_data <- read.csv("data/sections.csv")

# Join the tables
colnames(authors_data)[1] <- "authorID"
colnames(news_data)[1] <- "articleID"
data <- merge(news_data, authors_data, by = "authorID")
colnames(data)[colnames(data) == "name"] <- "author"

# Number of news published each year
data_publishing_year <- as.numeric(format(
  as.Date(data$date, "%B %d, %Y"), "%Y"
))

png(file = "docs/img/histogram_year.png")
hist(data_publishing_year,
  breaks = 20, xlab = "Year", xlim = c(2005, 2025),
  main = "Histogram of news' year of publishing", col = "lightblue",
  ylim = c(0, 2000),
)
dev.off()


# Frequency of authors (at least 100 articles)
table_authors <- table(data$author)
frequent_authors <- data[
  data$author %in% names(table_authors[table_authors > 100]),
]
png(file = "docs/img/plot_authors.png")
barplot(sort(table(frequent_authors$author), decreasing = TRUE),
  las = 2, cex.names = 0.6,
  main = "Frequency of articles by authors with at least 100 articles",
  col = "lightblue"
)
dev.off()

# Frequency of tags
png(file = "docs/img/plot_tags.png")
barplot(head(sort(table(tags_data$tag), decreasing = TRUE), 20),
  las = 2, cex.names = 0.6,
  main = "Frequency of tags in published articles",
  col = "lightblue"
)
dev.off()

# Frequency of sections
png(file = "docs/img/plot_sections.png")
# barplot(head(sort(table(sections_data$section), decreasing = TRUE), 20),
#   las = 2, cex.names = 0.6,
#   main = "Frequency of sections from published articles",
#   col = "lightblue"
# )
pie(head(sort(table(sections_data$section), decreasing = TRUE), 7), cex = 1)
dev.off()


