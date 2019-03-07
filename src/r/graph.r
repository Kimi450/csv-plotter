library(lattice)

df <- read.csv("processed-csv/processed_acc.csv")
# df <- head(df, n=1000)

names(df)

dev.new(width=30, height=6, unit="in")

df$Date <- strptime(as.character(df$Date), "%d/%m/%Y")
df$Date <- as.Date(df$Date, "%Y-%m-%d")

xyplot(Balance~Date,
       data=df,
       type="l",
       auto.key=list(space='right'))

dev.off()
# abline(lm(Date~Balance))
# title("hi")
