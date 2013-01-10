# Important Note: Arrays in R are labeled from 1 to n, but vertices in igraph are labled from 0 to n-1. This means V(G)[0]$name = V(G)$name[1]

PATH = "/media/data3/roja/Balatarin/CompleteRun/Results/"
library(igraph)
# read graph from file
G<-read.graph("unipartite.txt", format="ncol")
#sink(file="BalatarinModularity.txt",append=TRUE,type="output")
# cluster the base graph and save membership information
source("clustergraph.R")
results <- clustergraph(G)
memberships <- list(membership=results$membership,csize=results$csize)
modularity <- results[3]
# save the names of vertices belonging to each cluster in a separate file.
N= length(memberships$csize)
source("vertexwrite.R")
vertexwrite(memberships,G,'memberships')
#write(modularity[[1]],file="modularity",ncolumns=1)
write(c(getwd(),N,modularity[[1]]),file=paste(PATH,"NumComsAndModularities",sep=""),ncolumns=3,append=TRUE)

