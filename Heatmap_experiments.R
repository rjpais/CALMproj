# HEATMAP WITH OBSERVED EXPERIMENTAL ACTIVITY & RESPECTIVE WEIGHTS

# Load the data file EXP_DATA.csv with activity 
data <-  read.csv (file.choose())

# generate a matrix with the experimental data
M_SS <- data.matrix( data[, 2:ncol(data)])

# Names for each row in the matrix rows with stable states names from data text file. 
ss_lables <- data[,1]
rownames(M_SS) <- ss_lables


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

Select_colors <- c ("lightgray", "cyan","blue", "darkblue")
Hmap_col <- colorRampPalette (Select_colors) (n =399)

#collor Limits for the heatmap

col_breaks = c (seq(0,3,length=100), seq(10,14,length=100), seq(15,25,length=100),
               seq(26,30,length=100)) 
  

# heatmap generation  with nodes and states in 2 different positions    
# In alternative... a transpose of the heatmap by substitute M_SS fot t(M_SS) and adjust margins to (8,6)


par (mar = c(1,1,1,1))
            
heatmap.2 ( M_SS, col= Hmap_col, breaks=col_breaks,dendrogram="none",  trace="none",
          tracecol="white", vline = NULL, hline = NULL,
            density.info="none", Colv=FALSE, Rowv ="none", notecol="black", margins = c(10,11), keysize =1)


LEGEND_NAMES <- c ("not observed", "Decrease","Similar", "Increase")
Vcolor <- c ("gray", "cyan","blue", "darkblue")

legend("top", inset=0.1, LEGEND_NAMES, fill=Vcolor , horiz = TRUE, cex=0.7 )








