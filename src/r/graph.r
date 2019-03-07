library(lattice)

file <- read.csv("processed-csvmk/processed_acc.csv")

file <- head(file, n=200)

names(file)

dev.new(width=60, height=6, unit="in")

xyplot(Balance~Date,
       data=file,
       type="l",
       auto.key=list(space='right'))

dev.off()
# abline(lm(Date~Balance))
# title("hi")
