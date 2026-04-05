var <- read.csv(file.choose(), sep = ",", header = TRUE)
summary(var)

var.test(var$time_g1, var$time_g2, alternative = "two.sided")
#null hypo
#alternative 