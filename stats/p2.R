# CODE 1 — ONE SAMPLE T-TEST
# Apple sold in a day are 97
# H0: mu = 97
# H1: mu < 97 (one-tailed, less)
apple <- read.csv(file.choose(), sep = ",", header = TRUE)
summary(apple)
t.test(apple$C1, alternative = "less", mu = 97)


# CODE 2 — TWO SAMPLE INDEPENDENT T-TEST
# Assessing difference in salary of males and females
# H0: Average salary is equal for both groups
# H1: Average salary is not equal
Salary <- read.csv(file.choose(), sep = ",", header = TRUE)
summary(Salary)
t.test(Salary$MALES, Salary$FEMALES,
       alternative = "two.sided",   # FIX: "two.side" → "two.sided"
       var.equal = TRUE)

# CODE 3 — PAIRED T-TEST
# Survey to check poverty level
# H0: Poverty has not increased (difference = 0)
# H1: Poverty has increased (X1 > X2)
poverty <- read.csv(file.choose(), sep = ",", header = TRUE)
summary(poverty)
t.test(poverty$X1, poverty$X2,
       alternative = "greater",
       paired = TRUE)

# CODE 4 — PAIRED T-TEST
# MIS Report: Check if time after is less than time before
# H0: Average time is equal (before and after)
# H1: Average time after is less than before
time1 <- read.csv(file.choose(), sep = ",", header = TRUE)
summary(time1)
t.test(time1$time_before, time1$time_after,
       alternative = "greater",   
       paired = TRUE)

# CODE 5 — CORRELATION T-TEST
# Study correlation between aptitude and job proficiency
# H0: No correlation between aptitude and job proficiency (r = 0)
# H1: Aptitude and job proficiency are correlated

cor_data <- read.csv(file.choose(), sep = ",", header = TRUE)  
summary(cor_data)
cor.test(cor_data$aptitude, cor_data$job_prof,
         alternative = "two.sided",
         method = "pearson")