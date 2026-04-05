# Install packages if needed
install.packages(c("MASS", "ROCR"))

library(MASS)
library(ROCR)

data(biopsy)
head(biopsy)
str(biopsy)

# Remove ID column - not required for modelling
biopsy$ID = NULL

# Rename column headings
names(biopsy) = c("thick","usize","ushape","adhsn","celsiz","nucl","chrom","nuclus","mit","class")

# Data cleaning - check for NA fields
colSums(is.na(biopsy))

# Remove NA rows
biopsy1 = na.omit(biopsy)

set.seed(123)

# Split into 70:30 train/test
ind = sample(2, nrow(biopsy1), replace = TRUE, prob = c(0.7, 0.3))
train = biopsy1[ind == 1, ]
test  = biopsy1[ind == 2, ]

# Fit logistic regression on training data
fullfit = glm(class ~ ., family = binomial, data = train)
summary(fullfit)

# Predict probabilities on test data
test$prob = predict(fullfit, newdata = test, type = "response")  

# Get actual number of rows in test set dynamically
n_test = nrow(test)

# Make predictions: >0.5 probability = malignant
test$predict = rep("benign", n_test)              
test$predict[test$prob > 0.5] = "malignant"     

# Confusion matrix
table(test$predict, test$class)

# Accuracy
mean(test$predict == test$class)

# ROC Curve
ROCRpred = prediction(test$prob, test$class)
ROCRperf = performance(ROCRpred, "tpr", "fpr")  
plot(ROCRperf, colorize = TRUE)

# AUC
auc = performance(ROCRpred, "auc")               
auc@y.values