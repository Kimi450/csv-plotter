library(lattice)
file <- read.csv("processed_acc.csv")

file <- head(file, n=20)

names(file)

jpeg('plot.jpg')

xyplot(Balance~Date,
       data=file,
       type="l",
       auto.key=list(space='right'))

dev.off()
# abline(lm(Date~Balance))
# title("hi")
