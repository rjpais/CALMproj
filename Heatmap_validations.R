# HEATMAP WITH THE STABLE STATES OBTAINED FROM MODEL VERSUS THE OBSERVED EXPERIMENTAL DATA

# Load the data for sable states obtained by similation and experimental observations 
# Choose the csv file containing stable states from simulations and experimental data")
#            A B C D ... line 1 (line with node names)
# EXPi       1   1   ... line 2 (nine wiyh the experimental data) 
# SIMi       1 1 1 1 ... line 3 (line with stable states from model)
# blank spots for nodes that there is no information about experimental data. 
# The file must have the names of colums and rows in first positions")
data <-  read.csv (file.choose())

M_EXP <- data.matrix( data[1:13, 2:44])
M_SIM <- data.matrix( data[16:28, 2:44])

MAX_values <- as.vector(as.numeric( data[14, 2:44]))
M_MAX=  rbind(MAX_values, MAX_values, MAX_values, MAX_values, MAX_values, MAX_values, MAX_values, MAX_values, MAX_values, MAX_values, MAX_values, MAX_values, MAX_values)

InitialSS  <- as.vector(as.numeric( data[15, 2:44]))
M_InitialSS = rbind(InitialSS,InitialSS,InitialSS,InitialSS,InitialSS,InitialSS,InitialSS,InitialSS, InitialSS,InitialSS,InitialSS,InitialSS,InitialSS ) 
  
VARs=M_SIM/M_MAX  - M_InitialSS/M_MAX
M_SIM_var= (round( (VARs + 0.2*VARs)) + 2 )*10
  

M_CHECK= M_EXP/M_SIM_var *10
  

# Names for each row in the matrix rows with stable states names from data text file. 
ss_lables <- data[1:13,1]
rownames(M_CHECK) <- ss_lables

# Necessary graphical packages for proper heatmap.2 

require(grDevices)
if (!require("gplots")) {
  install.packages("gplots", dependencies = TRUE)
  library(gplots)}

if (!require("RColorBrewer")) {
  install.packages("RColorBrewer", dependencies = TRUE)
  library(RColorBrewer)}

if (!require("Matrix")) {
  install.packages("Matrix", dependencies = TRUE)
  library(Matrix)}


#Defining the colors used in the heatmap

Select_colors <- c ("gray", "red","red", "green", "red", "red")
Hmap_col <- colorRampPalette (Select_colors) (n =599)

#collor Limits for the heatmap

col_breaks = c (seq(0,1,length=100), seq(3, 5,length=100), seq(6, 9,length=100),seq(9.5,10,length=100),
                seq(11, 15,length=100), seq(16,30,length=100)) 
  

# heatmap generation  with nodes and states in 2 different positions    
# In alternative... a transpose of the heatmap by substitute M_SS fot t(M_SS) and adjust margins to (8,6)




heatmap.2 ( M_CHECK, col= Hmap_col, breaks=col_breaks,dendrogram="none",
           trace="none",tracecol="white", vline = NULL, hline = NULL,
            density.info="none", Colv="NA", Rowv ="NA", notecol="black", margins = c(16,8), cellnote = M_SIM, keysize = 1)



LEGEND_NAMES <- c ("Not tested","Compatible", "Incompatible")
Vcolor <- c ("gray","green", "red")
legend("bottom", inset=0.005, LEGEND_NAMES, fill=Vcolor , horiz = TRUE, cex=0.8 )




