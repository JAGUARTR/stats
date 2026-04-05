library(dplyr)

head(iris)         
summary(iris)


my_data <- as_tibble(iris)
my_data

#summary
my_data %>%
  summarise(
    count    = n(),
    mean_sep = mean(Sepal.Length, na.rm = TRUE),
    mean_pet = mean(Petal.Length, na.rm = TRUE)
  )

#  Mean 
my_data %>%
  group_by(Species) %>%
  summarise(
    count    = n(),
    mean_sep = mean(Sepal.Length),
    mean_pet = mean(Petal.Length)
  )

my_data %>%
  group_by(Species) %>%
  summarise_all(mean)

my_data %>%
  group_by(Species) %>%
  summarise(
    count      = n(),
    median_sep = median(Sepal.Length),
    sdev_pet   = sd(Petal.Length)
  )

# IQR
my_data %>%
  group_by(Species) %>%
  summarise(
    count   = n(),
    IQR_sep = IQR(Sepal.Length),
    IQR_pet = IQR(Petal.Length)
  )