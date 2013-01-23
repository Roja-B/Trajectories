#"! 
	myclusterVec<-append(myclusterVec,c$no)
	print(c$}
	myclusterVec<-append(myclusterVec,c$no)
	myclusterVec<-append(myclusterVec,c$no)
	print(c$no)
	c <- clusters(Gi)
	Gi <-}
	myclusterVec<-append(myclusterVec,c$no)
	print(c$no)
	c <- clusters(Gi)
	Gi <- subgraph(Gi,vi)
#	print(vi)
	vi <- vi[c(-ind)]
	vi <-c(0:L)
	L = length(V(Gi)) - 1
	ind <- ind+1
	ind = which.max(degree(Gi))
for (j in 1:N){
#indeces<- sort.int(di,index.return=TRUE,decreasing=TRUE)$ix
myclusterVec<-c()
N=1000


library(igraph)
# this program removes high-degree nodes from the graph one by one and creates a vector of number of communities detected 
clustergraph<-function(G){
# Run Girvan-Newman's fast-greedy algoithm for community detection:
fgreedy<-fastgreedy.community(G,merges=TRUE, modularity=TRUE,weights=E(G)$weight)
memberships <-community.to.membership(G, fgreedy$merges, steps=which.max(fgreedy$modularity)-1)
print(paste('Number of detected communities=',length(memberships$csize)))
print('Community sizes = ')
print(memberships$csize)
modularity <- max(fgreedy$modularity)
#print(paste('Modularity = ',modularity))
return(c(memberships,modularity))
library(igraph)
#iterateClusters <- function(memberships, G, name){
#for (i in 0:(length(memberships$csize)-1)){
#	Vi=which(memberships$membership==i)-1 # V is the index of nodes in V(G) that belong to community i
#	Gi=subgraph(G,Vi) # V(Gi) will have the "names" of the nodes in V(G) that belong to community i
N=1000
myclusterVec<-c()
#indeces<- sort.int(di,index.return=TRUE,decreasing=TRUE)$ix
for (j in 1:N){
	ind = which.max(degree(Gi))
	ind <- ind+1
	L = length(V(Gi)) - 1
	vi <-c(0:L)
	vi <- vi[c(-ind)]
#	print(vi)
	Gi <- subgraph(Gi,vi)
	c <- clusters(Gi)
	print(c$no)
	myclusterVec<-append(myclusterVec,c$no)



# Important Note: Arrays in R are labeled from 1 to n, but vertices in igraph are labled from 0 to n-1. This means V(G)[0]$name = V(G)$name[1]
library(igraph)
# read graph from file
G<-read.graph("unipartite_edgelist.txt", format="ncol")
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


vertexwrite <- function(memberships, G, name){
for (i in 0:(length(memberships$csize)-1)){
	Vi=which(memberships$membership==i)-1 # V is the index of nodes in V(G) that belong to community i
	Gi=subgraph(G,Vi) # V(Gi) will have the "names" of the nodes in V(G) that belong to community i
	filename=paste('VertexCom',name,i)
	write(V(Gi)$name,file=filename,ncolumns=1)
#	filename = paste('G',name,i)
#	write(Gi,file=filename)
	filename=paste("VertexIndex",name,i)
	write(Vi,file=filename,ncolumns=1)
