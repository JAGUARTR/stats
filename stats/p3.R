# CODE 1 — ONE SAMPLE Z-TEST
# H0: Mean IQ is equal to 100
# H1: Mean IQ is not equal to 100
library(BSDA)

# Enter IQ levels for 20 patients
data <- c(88, 92, 94, 94, 96, 97, 97, 97, 99, 99,
          105, 109, 109, 109, 110, 112, 112, 113, 114, 115)

# Perform one sample z-test
z.test(data, mu = 100, sigma.x = 15)

# CODE 2 — TWO SAMPLE Z-TEST
# H0: Difference in means is equal to 0
# H1: Difference in means is not equal to 0
install.packages("BSDA")
library(BSDA)

# Enter IQ levels for 20 individuals from each city
cityA <- c(88, 92, 94, 94, 96, 97, 97, 97, 99, 99,
           105, 109, 109, 109, 110, 112, 112, 113, 114, 115)

cityB <- c(90, 91, 91, 91, 95, 95, 99, 99, 108, 109,
           109, 114, 115, 116, 117, 117, 128, 129, 130, 133)

# Perform two sample z-test
z.test(x = cityA, y = cityB, mu = 0, sigma.x = 15, sigma.y = 15)