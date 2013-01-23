#"! 
vertexwrite(memberships,G,'memberships')
source("vertexwrite.R")
N= length(memberships$csize)
# save the names of vertices belonging to each cluster in a separate file.
modularity <- results[3]
memberships <- list(membership=results$membership,csize=results$csize)
results <- clustergraph(G)
source("clustergraph.R")
# cluster the base graph and save membership information
sink(file="BalatarinModularity.txt",append=TRUE,type="output")
G<-read.graph("unipartite.txt", format="ncol")
# read graph from file
library(igraph)
# Important Note: Arrays in R are labeled from 1 to n, but vertices in igraph are labled from 0 to n-1. This means V(G)[0]$name = V(G)$name[1]
