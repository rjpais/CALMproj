# Generates piecharts of the reached stable states in specific biological scenarios. 


#PROBABILITIES (%) OF REACHED PHENOTYPES

# WILD TYPE :  RPTP=0 DELTA=0 FAT4L=0 
# Phen.     E1   E2   E3   H    M1   M2
P1WT  <- c( 65 ,  0 ,  0 ,  0 ,  0 ,  35 ) # NORMAL TISSUE
P2WT  <- c( 0 ,  0 ,  0 ,  0 ,  100 ,  0 ) # TISSUE GROWTH
P3WT  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # INFLAMMATION
P4WT  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION
P5WT  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION + HYPOXIA

# WILD TYPE : DELTA=0 FAT4L=0"
P6WT  <- c( 100 ,  0 ,  0 ,  0 ,  0 ,  0 ) # NORMAL TISSUE
P7WT  <- c(53 ,  0 ,  0 ,  0 ,  47 ,  0 ) # TISSUE GROWTH
P8WT  <- c( 100 ,  0 ,  0 ,  0 ,  0 ,  0 ) # INFLAMMATION
P9WT  <- c( 0 ,  0 ,  100 ,  0 ,  0 ,  0 ) # CHRONIC INFLAMMATION
P10WT  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION + HYPOXIA



# SRC E1 :  RPTP=0 DELTA=0 FAT4L=0 
P1SRC  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # NORMAL TISSUE
P2SRC  <- c( 0 ,  0 ,  0 ,  0 , 100 ,  0 ) # TISSUE GROWTH
P3SRC  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # INFLAMMATION
P4SRC  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION
P5SRC  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION + HYPOXIA

# SRC E1 :  RPTP=1 DELTA=0 FAT4L=0 
P6SRC  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # NORMAL TISSUE
P7SRC  <- c( 0 ,  0 ,  0 ,  0 , 100 ,  0 ) # TISSUE GROWTH
P8SRC  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # INFLAMMATION
P9SRC  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION
P10SRC  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION + HYPOXIA


# TGFb E1 :  RPTP=0 DELTA=0 FAT4L=0 
P1TGF  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # NORMAL TISSUE
P2TGF  <- c( 0 ,  0 ,  0 ,  0 ,  100 ,  0 )# TISSUE GROWTH
P3TGF  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # INFLAMMATION
P4TGF  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION
P5TGF  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION + HYPOXIA

# TGFb E1 :  RPTP=1 DELTA=0 FAT4L=0 
P6TGF  <- c( 0 ,  0 ,  100 ,  0 ,  0 ,  0 ) # NORMAL TISSUE
P7TGF  <- c( 0 ,  0 ,  50 ,  0 ,  50 ,  0 )# TISSUE GROWTH
P8TGF  <- c( 0 ,  0 ,  100 ,  0 ,  0 ,  0 ) # INFLAMMATION
P9TGF  <- c( 0 ,  0 ,  100 ,  0 ,  0 ,  0 ) # CHRONIC INFLAMMATION
P10TGF  <- c( 0 ,  0 ,  0 ,  0 ,  0 ,  100 ) # CHRONIC INFLAMMATION + HYPOXIA


Vcolor <-   c("#FFA500", "#8F8013" , "#8B6914" ,  "#BDB76B" , "#FFC0CB", "#6CA6CD")

Phen <- c("F=0 & C=2", "F=0 & C=1", "F=1 & C=2", "F=1 & C=1" ,  "F=0 & C=0", "F=1 & C=0")


#Pie chart with probabilities


# The comparison of RPTP  activation in WT  

par(mai=c(1,0.1, 0.2,0.1))
pie(P1WT, labels = Phen , col = Vcolor, main= "Wild-type reachability with no input signals", clockwise = FALSE )
legend("bottom", inset=0.01, Phen, fill=Vcolor , horiz = TRUE, cex=0.8 )


par(mfrow=c(2,5), mai=c(0.1,0.5, 0.1,0.1))

# WILD-type with RPTP =0 FAT4L =0 DELTA =0
pie(P1WT, labels = "" , col = Vcolor)
pie(P2WT, labels = "" , col = Vcolor)
pie(P3WT, labels = "" , col = Vcolor)
pie(P4WT, labels = "" , col = Vcolor)
pie(P5WT, labels = "" , col = Vcolor)

# WILD-type with RPTP =0 FAT4L =0 DELTA =0
pie(P6WT, labels = "" , col = Vcolor)
pie(P7WT, labels = "" , col = Vcolor)
pie(P8WT, labels = "" , col = Vcolor)
pie(P9WT, labels = "" , col = Vcolor)
pie(P10WT, labels = "" , col = Vcolor)




# The comparison of RPTP  activation in SRC  E1 
# RPTP =0 FAT4L =0 DELTA =0
pie(P1SRC,labels = "", col = Vcolor)
pie(P2SRC,labels = "", col = Vcolor )
pie(P3SRC,labels = "", col = Vcolor)
pie(P4SRC,labels = "", col = Vcolor)
pie(P5SRC,labels = "", col = Vcolor)
# RPTP =1 FAT4L =0 DELTA =0
pie(P6SRC,labels = "", col = Vcolor)
pie(P7SRC,labels = "", col = Vcolor )
pie(P8SRC,labels = "", col = Vcolor)
pie(P9SRC,labels = "", col = Vcolor)
pie(P10SRC,labels = "", col = Vcolor)




# The comparison of RPTP  activation in TGFb E1 
# RPTP =0 FAT4L =0 DELTA =0
pie(P1TGF, labels = "", col = Vcolor)
pie(P2TGF, labels = "", col = Vcolor)
pie(P3TGF, labels = "", col = Vcolor)
pie(P4TGF, labels = "", col = Vcolor)
pie(P5TGF, labels = "", col = Vcolor)
# RPTP =1 FAT4L =0 DELTA =0
pie(P6TGF, labels = "", col = Vcolor)
pie(P7TGF, labels = "", col = Vcolor)
pie(P8TGF, labels = "", col = Vcolor)
pie(P9TGF, labels = "", col = Vcolor)
pie(P10TGF, labels = "", col = Vcolor)


