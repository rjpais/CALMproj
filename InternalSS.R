
# input txt files with names of perturbations  
header1 <- readLines(file.choose())
names <- c (unlist(strsplit(header1[1], " ") ))   


#input file with the internal stable states
raw_data1 <-  readLines (file.choose())

Phenotype <-  c (raw_data1[1]) 


num_components <- length(names)                  

# Generate a list of strings for the stable states and a vector of stable states lables 
SS_LIST <-  c(raw_data1[2: length(raw_data1)])
SS_values <- c(unlist(strsplit(SS_LIST[1: length(SS_LIST)], "")))  # Separate characters from string and convert into a vector  


# Replace non-numeric characters with a number (not 0,1 and 3) with a numeric value for each color  

# Red color values 
Val_matrix <- c(gsub("0", "5", SS_values, fixed=TRUE)) 

# light and dark green colors 
Val_matrix <- c(gsub("1", "15", Val_matrix, fixed=TRUE)) 
Val_matrix <- c(gsub("2", "25", Val_matrix, fixed=TRUE))
Val_matrix <- c(gsub("*", "38", Val_matrix, fixed=TRUE))
Val_matrix <- c(gsub("-", "50", Val_matrix, fixed=TRUE))
Val_matrix <- c(gsub("a", "50", Val_matrix, fixed=TRUE))
Val_matrix <- c(gsub("b", "50", Val_matrix, fixed=TRUE))
Val_matrix <- c(gsub("c", "50", Val_matrix, fixed=TRUE))
Val_matrix <- c(gsub("_", "60", Val_matrix, fixed=TRUE))
Val_matrix <- c(gsub("?", "60", Val_matrix, fixed=TRUE))



# Transformes the characteres into numeric values in generates a matrix with dimentions: Stable states x number of components
Values_SS <- c(as.numeric(Val_matrix))
M_SS <- as.matrix(array(Values_SS, dim = c(num_components , length(SS_LIST) )))


# Values for showing in the matrix 
matrix_lables <- as.matrix(array(SS_values, dim = c(num_components, length(SS_LIST) )))


# Names of components in the matrix. 
rownames(M_SS) <- c(names)
colnames(M_SS) <- NULL

# necessary graphical packages for heatmap.2 
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


#Defining the colors for heatmap

Select_colors <- c ("red", "green","darkgreen", "gray", "yellow", "white" )
Hmap_col <- colorRampPalette (Select_colors) (n =499)

# defining colors tresholds and gradients for the heatmap

col_breaks = c (seq(0,8,length=100), seq(10, 20 , length=100), seq(22, 28,length=100),seq(30, 38,length=100), seq(40, 50, length=100), seq(41, 60, length=100) )
  

  
# heatmap plot generation  
 
heatmap.2 ( t(M_SS), col = Hmap_col, dendrogram="none", main = Phenotype,
            trace="none",tracecol="black", density.info="none", Colv="NA", Rowv ="NA", cellnote= t(matrix_lables), notecol="black",  margins = c(10,10), cexRow = 1)

#legend("left", inset=0.001, c("basal", "high/intermediate" , "high", "variable"), fill= c("red", "green", "darkgreen", "yellow") , horiz = FALSE, cex=0.8 )

