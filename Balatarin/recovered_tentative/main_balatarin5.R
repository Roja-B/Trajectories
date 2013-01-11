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
write(c(getwd(),N,modularity[[1]]),file=paste(PATH,"NumComsAndModularities",sep=""),ncolumns=2,append=TRUE)
vertexwrite <- function(memberships, G, name){
write(c("com","vertices","edges","density"),file="communityStats",ncolumns=4)
for (i in 0:(length(memberships$csize)-1)){
        Vi=which(memberships$membership==i)-1 # V is the index of nodes in V(G) that belong to community i
        if (length(Vi)<4){
                write(c(i,length(Vi),"NA","NA"),file="communityStats",ncolumns=4,append=TRUE)
                next}
        Gi=subgraph(G,Vi) # V(Gi) will have the "names" of the nodes in V(G) that belong to community i
        filename=paste('community',i,sep="")
        write(V(Gi)$name,file=filename,ncolumns=1)
#       filename = paste('G',name,i)
#       write(Gi,file=filename)
        filename=paste("VertexIndex",name,i,sep="")
        write(Vi,file=filename,ncolumns=1)
# here report size and density of each com
        stats<- c(i,length(V(Gi)),length(E(Gi)),graph.density(Gi))
        write(stats,file="communityStats",ncolumns=4,append=TRUE)
        pagerank <- page.rank(Gi,vids=V(Gi),directed=FALSE,weights=E(Gi)$weight)
        filename = paste("pageranks",i,sep="")
        write(pagerank$vector,file=filename,ncolumns=1)

"after saving bipartite and unitpartite graphs:
the file NumComsAndModularities will have directory name, number of coms, and modularity
note: if number of nodes is less than 3 we should move on (com-finding will fail)
this issue also exists for any communities with less than 3 nodes
results are going to be in directory ResultsJaccard30day14slide
"

