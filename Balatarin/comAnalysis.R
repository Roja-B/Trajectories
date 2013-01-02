library(igraph)
#iterateClusters <- function(memberships, G, name){
#for (i in 0:(length(memberships$csize)-1)){
#	Vi=which(memberships$membership==i)-1 # V is the index of nodes in V(G) that belong to community i
#	Gi=subgraph(G,Vi) # V(Gi) will have the "names" of the nodes in V(G) that belong to community i
#}
#}

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
}
