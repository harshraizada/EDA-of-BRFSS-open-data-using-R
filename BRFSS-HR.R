getwd()
setwd("/Users/harsh/Desktop/R-project")
library(SASxport) #installed package to read .XPT file
library(ggplot2) # installed package for plots
library(dplyr) # For grouping of data and other functions
library(car) # To recode the variable responses
library(ggthemes) # installed theme package for plots
brfss=read.xport("LLCP2016.XPT ")# reading of LLCP2016.XPT file into brfss reading file
write.csv(brfss,file="brfssp.csv")
brfssp=read.csv("brfssp.csv")
dim(brfssp)
cbrfss=brfss #copy of data set brfss
cbrfss[] <- lapply(cbrfss, unclass) # l apply to change from labelled integer to integer
brfssci=subset(cbrfss,DISPCODE==1100) #Data frame having those respondent data who has completed interview
brfssvarList <- c("GENHLTH","HLTHPLN1","EXERANY2","SEX","MARITAL","EDUCA",
                  "VETERAN3","EMPLOY1","SMOKE100","SMOKDAY2","FLUSHOT6","SEATBELT"
                  ,"ADDEPEV2") # working variable list by removing unecessary variables
brfssciwd=brfssci[brfssvarList]
str(brfssciwd)

#Objective-1 To find out the perception of the people about their existing general health status among US residents. 

GEONA=na.omit(brfssciwd$GENHLTH) # Data cleaning by removing NA
GEONADF=as.data.frame(GEONA) # converted to data frame
GE=group_by(GEONADF,GEONA) # group by function
GE1=dplyr::summarise(GE,Frequency=n())%>% mutate(Percentage=Frequency/sum(Frequency)*100) #summarise function

GE1$GEONA=recode(GE1$GEONA,"1='Excellent';2='Very Good';3='Good';4='Fair';5='Poor';7='Dont Know';9='Refused'")

ggplot(aes(x=reorder(GEONA,-Percentage),y=Percentage),data = GE1)+
  geom_bar(stat="identity",width = 0.5,aes(fill=GEONA),colour="black")+
  ggtitle('Perception of the people about their existing general health status among US residents')+
  geom_text(aes(label=Percentage,vjust=-0.5))+
  xlab('General Health Status')+
  ylab("Percentage(%)")+
  theme_linedraw()+
  theme(plot.title = element_text(size = 12),
        axis.title = element_text(size = 12,face="bold"))

#Objective-2 To find out the existing health care coverage rate among US residents.
HLTP=group_by(brfssciwd,HLTHPLN1)
HLTP1=dplyr::summarise(HLTP,Frequency=n())%>% mutate(Percentage=Frequency/sum(Frequency)*100)
HLTP1$HLTHPLN1=recode(HLTP1$HLTHPLN1,"1='Yes';2='No';7='Dont Know';9='Refused'")
ggplot(aes(x=reorder(HLTHPLN1,-Percentage),y=Percentage),data = HLTP1)+
  geom_bar(stat="identity",width = 0.5,aes(fill=HLTHPLN1),colour="black")+
  ggtitle('Existing health care coverage rate among US residents')+
  geom_text(aes(label=Percentage,vjust=-0.5))+
  xlab('Health Care Coverage Status')+
  ylab("Percentage(%)")+
  theme_linedraw()+
  theme(plot.title = element_text(size = 12),
        axis.title = element_text(size = 12,face="bold"))

#Objective-3 To find out the existing exercise or physical activity rates among US residents.
EXE=group_by(brfssciwd,EXERANY2)
EXE1=dplyr::summarise(EXE,Frequency=n())%>% mutate(Percentage=Frequency/sum(Frequency)*100)
EXE1$EXERANY2=recode(EXE1$EXERANY2,"1='Yes';2='No';7='Dont Know';9='Refused'")
ggplot(aes(x=reorder(EXERANY2,-Percentage),y=Percentage),data = EXE1)+
  geom_bar(stat="identity",width = 0.5,aes(fill=EXERANY2),colour="black")+
  ggtitle('Exercise or physical activity rates among US residents')+
  geom_text(aes(label=Percentage,vjust=-0.5))+
  xlab('Exercise or physical activity Status')+
  ylab("Percentage(%)")+
  theme_linedraw()+
  theme(plot.title = element_text(size = 12),
        axis.title = element_text(size = 12,face="bold"))

#Objective-4 To find out the existing smoking rate of respondents who have ever smoked in their life.

SMO=group_by(brfssciwd,SMOKE100)
SMO1=dplyr::summarise(SMO,Frequency=n())%>% mutate(Percentage=Frequency/sum(Frequency)*100)
SMO1$SMOKE100=recode(SMO1$SMOKE100,"1='Yes';2='No';7='Dont Know';9='Refused'")
ggplot(aes(x=reorder(SMOKE100,-Percentage),y=Percentage),data = SMO1)+
  geom_bar(stat="identity",width = 0.5,aes(fill=SMOKE100),colour="black")+
  ggtitle('smoking rate of respondents who have ever smoked in their life')+
  geom_text(aes(label=Percentage,vjust=-0.5))+
  xlab('Ever Smoked')+
  ylab("Percentage(%)")+
  theme_linedraw()+
  theme(plot.title = element_text(size = 12),
        axis.title = element_text(size = 12,face="bold"))

#Objective-5 To find out the current smoking status of the respondent who ever smoked in their life. 
SS=subset(brfssciwd,SMOKE100==1)
SS1=group_by(SS,SMOKDAY2)
SS2=dplyr::summarise(SS1,Frequency=n())%>% mutate(Percentage=Frequency/sum(Frequency)*100)
SS2$SMOKDAY2=recode(SS2$SMOKDAY2,"1='Every Day';2='Some Days';3='Not at all';7='Dont know';9='Refused'")
ggplot(aes(x=reorder(SMOKDAY2,-Percentage),y=Percentage),data = SS2)+
  geom_bar(stat="identity",width = 0.5,aes(fill=SMOKDAY2),colour="black")+
  ggtitle('current smoking status of the respondent who ever smoked in their life')+
  geom_text(aes(label=Percentage,vjust=-0.5))+
  xlab('Current Smoking Status')+
  ylab("Percentage(%)")+
  theme_linedraw()+
  theme(plot.title = element_text(size = 12),
        axis.title = element_text(size = 12,face="bold"))

#Objective -6 To find out the existing coverage rate of flu vaccine among US residents.
FLU=group_by(brfssciwd,FLUSHOT6)
FLU1=dplyr::summarise(FLU,Frequency=n())%>% mutate(Percentage=Frequency/sum(Frequency)*100)
FLU1$FLUSHOT6=recode(FLU1$FLUSHOT6,"1='Yes';2='No';7='Dont Know';9='Refused'")
ggplot(aes(x=reorder(FLUSHOT6,-Percentage),y=Percentage),data = FLU1)+
  geom_bar(stat="identity",width = 0.5,aes(fill=FLUSHOT6),colour="black")+
  ggtitle('existing coverage rate of flu vaccine among US residents')+
  geom_text(aes(label=Percentage,vjust=-0.5))+
  xlab('Got Flu Vaccine in Past 12 month')+
  ylab("Percentage(%)")+
  theme_linedraw()+
  theme(plot.title = element_text(size = 12),
        axis.title = element_text(size = 12,face="bold"))

#Objective-7:To find out the existing seat belt usage practices (or rate) among US residents.
SB=group_by(brfssciwd,SEATBELT)
SB1=dplyr::summarise(SB,Frequency=n())%>% mutate(Percentage=Frequency/sum(Frequency)*100)
SB1$SEATBELT=recode(SB1$SEATBELT,"1='Always';2='Nearly Always';3='Sometime';4='Seldom';5='Never';7='Dont Know';8='Never Drive or Ride in a Car';9='Refused'")
ggplot(aes(x=reorder(SEATBELT,-Percentage),y=Percentage),data = SB1)+
  geom_bar(stat="identity",width = 0.5,aes(fill=SEATBELT),colour="black")+
  ggtitle('seat belt usage practices (or rate) among US residents')+
  geom_text(aes(label=Percentage,vjust=-0.5))+
  xlab('Seat Belt Usage Status')+
  ylab("Percentage(%)")+
  theme_linedraw()+
  theme(plot.title = element_text(size = 12),
        axis.title = element_text(size = 12,face="bold"))