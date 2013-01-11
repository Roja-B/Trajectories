# Important Note: Arrays in R are labeled from 1 to n, but vertices in igraph are labled from 0 to n-1. This means V(G)[0]$name = V(G)$name[1]
library(igraph)
# read graph from file
G<-read.graph("unipartite_edgelist.txt", format="ncol")
#G<-read.graph("unipartite_politics_12_2008-12_2008_5.txt", format="ncol")
sink(file="BalatarinModularity.txt",append=TRUE,type="output")
# cluster the base graph and save membership information
source("clustergraph.R")
results <- clustergraph(G)
memberships <- list(membership=results$membership,csize=results$csize)
modularity <- results[3]
# save the names of vertices belonging to each cluster in a separate file.
N= length(memberships$csize)
source("vertexwrite.R")
vertexwrite(memberships,G,'memberships')
