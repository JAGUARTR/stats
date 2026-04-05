# Install packages 
install.packages(c("nycflights13", "data.table", "forecast", "tsoutliers"))

library(nycflights13)
library(data.table)
library(forecast)
library(tsoutliers)

# Build data.table from nycflights13
dt <- data.table(flights)
dt[, date := ISOdate(year, month, day)]

daily <- dt[, list(
  N         = .N,
  Delays    = sum(arr_delay, na.rm = TRUE),
  Cancelled = sum(is.na(arr_delay)),   # cancelled flights have NA arr_delay
  Distance  = mean(distance, na.rm = TRUE)
), by = date]

str(daily)

# --- Time series of daily flight counts ---
nts <- ts(daily$N, frequency = 7)
plot(nts)

# --- ARIMA ---
auto.arima(nts)
auto.arima(nts, approximation = FALSE)   # fixed: was missing closing parenthesis

# --- Holt-Winters ---
fit <- HoltWinters(nts)
plot(fit)
forecast(fit)

f <- forecast(HoltWinters(nts), 5)
f
plot(f)

# --- Outlier detection on Cancellations ---
cts <- ts(daily$Cancelled)
fit <- auto.arima(cts)
auto.arima(cts)

outliers <- tso(cts, tsmethod = "arima", args.tsmethod = list(order = c(1, 1, 2)))
outliers
plot(outliers)

plot(tso(ts(daily$Cancelled)))