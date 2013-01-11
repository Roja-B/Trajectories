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


#############################################################
vertexwrite <- function(memberships, G, name){
for (i in 0:(length(memberships$csize)-1)){
	Vi=which(memberships$membership==i)-1 # V is the index of nodes in V(G) that belong to community i
	Gi=subgraph(G,Vi) # V(Gi) will have the "names" of the nodes in V(G) that belong to community i
	filename=paste('community',name,i,sep="")
	write(V(Gi)$name,file=filename,ncolumns=1)
#	filename = paste('G',name,i)
#	write(Gi,file=filename)
	filename=paste("VertexIndex",name,i,sep="")
	write(Vi,file=filename,ncolumns=1)
