
# Generates pie charts and barplots for the stable states that give specific phenotypes:
# unperturbed (wild-type) and perturbations (KO or Ectopic activation) 


# Vectors with the stable states of each phenotype for Wild-type and perturbations
# V <- c ( SS count epithelial, SS count Hybrid, SS count Amoeboid , SS count mesenchymal)

WT_00 <- c(2,2,0,0,0,64)
WT_01 <- c(2,34,0,0,0,64)
WT_10 <- c(33,0,0,0,0,32)
WT_11 <- c(33,33,0,0,0,32)

WT <- WT_00 + WT_01 + WT_10 + WT_11


WT2_00 <- c(4,3,0,0,8,56)
WT2_01 <- c(4,9,0,0,8,56)
WT2_10 <- c(18,1,16,0,0,32)
WT2_11 <- c(18,1,16,0,0,32)
WT2 <- WT2_00 + WT2_01 + WT2_10 + WT2_11


SRC_00 <- c(0,0,0,0,8,56)
SRC_01 <- c(0,8,0,0,8,56)
SRC_10 <- c(0,0,0,0,8,56)
SRC_11 <- c(0,8,0,0,8,56)
SRC <- SRC_00 + SRC_01 + SRC_10 + SRC_11



SRC2_00 <- c(0,0,0,0,8,56)
SRC2_01 <- c(0,8,0,0,8,56)
SRC2_10 <- c(16,0,16,0,0,32)
SRC2_11 <- c(16,0,16,0,0,32)
SRC2 <- SRC2_00 + SRC2_01 + SRC2_10 + SRC2_11

TGFb_00 <- c(0,0,0,0,8,56)
TGFb_01 <- c(0,4,0,0,8,56)
TGFb_10 <- c(0,0,32,0,8,48)
TGFb_11 <- c(0,4,32,0,8,48)
TGFb <- TGFb_00 + TGFb_01 + TGFb_10 + TGFb_11

TGFb2_00 <- c(0,0,0,0,8,56)
TGFb2_01 <- c(0,4,0,0,8,56)
TGFb2_10 <- c(0,0,32,0,0,48)
TGFb2_11 <- c(0,0,32,0,0,48)
TGFb2 <- TGFb2_00 + TGFb2_01 + TGFb2_10 + TGFb2_11


# Grouped barplot SETUP 

phenotypes <- c("F=0&C=2", "F=0&C=1", "F=2&C=1", "F=1&C=1",  "F=0&C=0", "F=1&C=0")
Bplot_limit = c(0, 100)
axis=1.2
pnames = 1.2
Vcolor <-   c("#FFA500", "#8B6914" , "#8F8013" ,  "#BDB76B" , "#FFC0CB", "#6CA6CD")

Plot_title = c("Effect of RPTPL and FAT4L")
vectors <- c( WT_00, WT_01, WT_10, WT_11) 
Dimension <- c(6,4)
Group_names <- c("RPTP- FAT4-", "RPTP- FAT4+", "RPTP+ FAT4-","RPTP+ FAT4+" )


# Barplot general  
Mic_count= as.matrix(array( vectors , dim = Dimension ))
colnames(Mic_count)  <- Group_names 
rownames(Mic_count) <- phenotypes 
barplot(Mic_count, main= Plot_title ,col = Vcolor, cex.axis = axis , cex.names = pnames , ylim = Bplot_limit1 , beside=TRUE)
legend("topright", inset=0.0, phenotypes, fill=Vcolor , horiz = TRUE, cex=0.7 )

