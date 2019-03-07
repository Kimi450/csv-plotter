library(lattice)
file <- read.csv("acc.csv")

file <- head(file, n=100)
# head(file, n=100)

names(file)

jpeg('rplot.jpg')

xyplot(Balance~Date, data=file, tpye="l",auto.key=list(space='right'))
dev.off()
# abline(lm(Date~Balance))
# title("hi")
