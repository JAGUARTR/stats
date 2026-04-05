# ONE WAY ANOVA
data1 <- read.csv(file.choose(), sep = ",", header = TRUE)
names(data1)
summary(data1)
head(data1)

# One-Way ANOVA
anv <- aov(formula = satindex ~ dept, data = data1)
summary(anv)

# Pairwise Comparison
TukeyHSD(anv)

# TWO WAY ANOVA
data2 <- read.csv(file.choose(), sep = ",", header = TRUE)
names(data2)
summary(data2)

# Two-Way ANOVA with interaction term
anv1 <- aov(formula = satindex ~ dept + exp + dept * exp, data = data2)
summary(anv1)