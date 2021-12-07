
library(openxlsx)
options(scipen = 200)
dfname <- list.files()

data <- read.csv(dfname[1],encoding = "UTF8")
for (i in 2:length(dfname)){
  data0 <- read.csv(dfname[i],encoding = "UTF8")
  data <- rbind(data,data0)
}
write.xlsx(data,file="out.xlsx")

dfname <- list.files()

data <- read.csv(dfname[1],encoding = "UTF8")
for (i in 2:length(dfname)){
  data0 <- read.csv(dfname[i],encoding = "UTF8")
  data <- rbind(data,data0)
}
write.xlsx(data,file="UK.xlsx")


dfname <- list.files()
data <- read.csv(dfname[1],encoding = "UTF8")
for (i in 2:length(dfname)){
  data0 <- read.csv(dfname[i],encoding = "UTF8")
  data <- rbind(data,data0)
}

q <- read.xlsx("US.xlsx")
out <- rbind(q,data)
out1 <- out[,c(4,5,6,9)]

write.xlsx(out1,file="data.xlsx")

options(scipen = 200)

dfname <- list.files()
data1 <- read.csv(dfname[1],encoding = "UTF8")
for (i in 2:length(dfname)){
  data0 <- read.csv(dfname[i],encoding = "UTF8")
  data1 <- rbind(data1,data0)
}


dfname <- list.files()
data2 <- read.csv(dfname[1],encoding = "UTF8")
for (i in 2:length(dfname)){
  data0 <- read.csv(dfname[i],encoding = "UTF8")
  data2 <- rbind(data2,data0)
}


dfname <- list.files()
data3 <- read.csv(dfname[1],encoding = "UTF8")
for (i in 2:length(dfname)){
  data0 <- read.csv(dfname[i],encoding = "UTF8")
  data3 <- rbind(data3,data0)
}


dfname <- list.files()
data4 <- read.csv(dfname[1],encoding = "UTF8")
for (i in 2:length(dfname)){
  data0 <- read.csv(dfname[i],encoding = "UTF8")
  data4 <- rbind(data4,data0)
}

library(dplyr)
library(stringr)

write.xlsx(data,"final.xlsx")
library(openxlsx)
library(stringr)
library(dplyr)

data <- read.xlsx("final.xlsx")
sen <- data$Description
word <- strsplit(sen,split = " ")
word <- unlist(word)

df <- table(word) %>%
  as.data.frame()

df <- df[order(df$Freq,decreasing = T),]

skill <- c()
q <- c('C', 'C++',' C#', 
       '.NET', 'Python', 
       'SQL', 'PHP', 'HTML', 
       'CSS', 'Bootstrap', 'Swift', 
       'Lua', 'MATLAB', 'jQuery', 
       'Git', 'TypeScript', 'Java', 'JavaScript', 
       'R', 'Ruby', 'Scala',  'Go', 'Node', 'React', 
       'Angular', 'Vue', 'Flask', 'Jinja', 'Django', 
       'MongoDB', 'Redis', 'Nginx', 'Cassandra', 
       'Hadoop', 'Express', 'Spark', 'REST', 'JSON', 
       'XML', 'Socket', 'Webpack', 'HTTPS', 'Spring MVC', 
       'Spring boot', 'Hibernat', 'Data structures', 
       'Algorithms', 'Multi-thread', 'Object Oriented Programming', 
       'Systems', 'Linux', 'PyTorch', 'TensorFlow', 'TCP/IP', 
       'GCC', 'Makefile')

for(i in 1:length(q)){
  q0 <- which(df$word==q[i])
  skill <- c(skill,q0)
}
df$word <- as.character(df$word)
out <- df[skill,]

colnames(out) <- c("Skill","Freq")

out <- out[order(out$Freq,decreasing = T),]
write.xlsx(out,"skill.xlsx")
