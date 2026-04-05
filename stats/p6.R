#    initiate a empty model 
forward_model <- step(
  lm(mpg ~ 1, data = mtcars),          
  direction = "forward",
  scope = formula(lm(mpg ~ ., data = mtcars)) 
)

# BACKWARD STEPWISE 
backward_model <- step(
  lm(mpg ~ ., data = mtcars),
  direction = "backward"
)

#  BOTH DIRECTIONS 
both_model <- step(
  lm(mpg ~ 1, data = mtcars),         
  direction = "both",
  scope = formula(lm(mpg ~ ., data = mtcars))
)

#  SCATTER PLOT
sorted_idx <- order(mtcars$hp)      

plot(mtcars$hp, mtcars$mpg,
     main = "Scatter Plot of mpg vs. hp",
     xlab = "hp", ylab = "mpg", pch = 20)

abline(lm(mpg ~ hp, data = mtcars), col = "Black", lwd = 2)

points(sort(mtcars$hp), forward_model$fitted.values[sorted_idx], 
       col = "Red",   pch = 20)
points(sort(mtcars$hp), backward_model$fitted.values[sorted_idx],
       col = "Blue",  pch = 20)
points(sort(mtcars$hp), both_model$fitted.values[sorted_idx],    
       col = "Green", pch = 20)

legend("topright",
       legend = c("Simple (hp only)", "Forward", "Backward", "Both-Direction"),
       col    = c("Black", "Red", "Blue", "Green"),
       pch    = c(NA, 20, 20, 20),
       lty    = c(1, NA, NA, NA))      