setwd("F:\\EXCEL R\\ASSIGNMENTS\\SIMPLE LINEAR REGRESSION")

dlv <- read.csv("delivery_time.csv")
View(dlv)
attach(dlv)
plot(Sorting.Time,delivery)
cor(Delivery.Time,Sorting.Time)
trial1 <- lm(Delivery.Time~Sorting.Time)
summary(trial1)
trial1$fitted.values
confint(trial1,0.95)
predict(trial1,inteval = "predict")
trial1$residuals
mean(trial1$residuals)

######Rsquared value=0.665, mean erroe=4.758099e-17
########12         3         4         5         6         7         8         9        10 
23.072933 13.178814 16.476853 21.423913 23.072933 16.476853 18.125873 11.529794 23.072933 21.423913 
11        12        13        14        15        16        17        18        19        20 
19.774893 13.178814 18.125873 11.529794 11.529794 13.178814 16.476853 18.125873  9.880774 18.125873 
21 
14.827833 





#######TRIAL 2
trial2 <- lm(Delivery.Time~log(Sorting.Time))
summary(trial2)
trial2$fitted.values
trial2$residuals
mean(trial2$residuals)
plot(trial2)
#### Rsquared value=0.6794, mean=-1.863589e-16
##1        2        3        4        5        6        7        8        9       10       11       12 
21.98291 13.69652 17.36331 21.03009 21.98291 17.36331 18.75735 11.09489 21.98291 21.03009 19.96493 13.69652 
13       14       15       16       17       18       19       20       21 
18.75735 11.09489 11.09489 13.69652 17.36331 18.75735  7.42810 18.75735 15.71450 



########trial3
trial3 <- lm(log(Delivery.Time)~Sorting.Time)
summary(trial3)
trial3$fitted.values
mean(trial3$residuals)
confint(trial3,level=0.95)
exp(predict(trial3,inteval="predict"))
#### R square value=0.69, mean= -2.312965e-18


#### therefore even though model 3 has better Rsquare value, the mean of the error is more compared to model 2. therefore model 2 is selected.
