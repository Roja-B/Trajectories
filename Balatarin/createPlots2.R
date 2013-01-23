#!/bin/bash
python prepare4R_NumComsAndModularities.py 
rm Work/RandIndecesOverTime_withUnsharedNodes.txt
python com_contingencytable_Rand.py
mkdir Results/ComContingencyTable100
mkdir Results/TransitionProbs
mv Results/ComContingencyTable* Results/ComContingencyTable100/
mv Results/TrProbs* Results/TransitionProbs/
cp createplots.R Work
cd Work
R --save < createplots.R
cd ..
graph_stats<-read.table("U-pol_J100VT_stats.txt",header=FALSE)
#graph_stats<-read.table("U-pol_L-VT5_stats.txt",header=FALSE)
ndates1 <- as.Date(graph_stats$V1, "%m%d%Y-%m%d%Y")
pdf("graphEdgesvsTime.pdf")
plot(ndates1,graph_stats$V3,main="Number of graph edges over sliding window",xlab="Window start date",ylab="Number of edges","l")
dev.off()
pdf("graphDensityvsTime.pdf")
plot(ndates1,graph_stats$V4,main="Graph density over sliding window",xlab="Window start date",ylab="Graph density","l")
dev.off()
pdf("graphSizevsTime.pdf")
plot(ndates1,graph_stats$V2,main="Graph size over sliding window",xlab="Window start date",ylab="Number of nodes (active users)","l")
dev.off()
clustering_stats<-read.table("NumComsAndModularities_betterformat",header=FALSE)
ndates2 <- as.Date(clustering_stats$V1, "%m%d%Y-%m%d%Y")
clustering_stats$ndates2<-ndates2
clustering_stats_ordered<-clustering_stats[order(ndates2),]
pdf("modularityVsTime.pdf")
plot(clustering_stats_ordered$ndates2,clustering_stats_ordered$V3,main="Modularity of detected communities over sliding window",xlab="Window start date",ylab="Modularity","l")
dev.off()
pdf("numComsVsTime.pdf")
plot(clustering_stats_ordered$ndates2,clustering_stats_ordered$V2,main="Number of communities over sliding window",xlab="Window start date",ylab="Number of communities in graph","l")
dev.off()
Randindex<-read.table("RandIndecesOverTime_withUnsharedNodes.txt",header=FALSE)
ndates3 <- as.Date(Randindex$V1, "%m%d%Y-%m%d%Y")
Randindex$ndates<-ndates3
pdf("RandvsTime.pdf")
plot(Randindex$ndates,Randindex$V2,main="Adjusted Rand index between consecutive clusterings",xlab="Window start date",ylab="Adjusted Rand index","l")
dev.off()
pdf("randPlusDensity.pdf")
plot(Randindex$ndates,Randindex$V2,main="rand index (black) and density (blue)","l")
lines(ndates1,graph_stats$V4,"l",col="blue")
dev.off()
colnames(graph_stats)<-c("timeWindow","nodes","edges","density")
pdf("randAndSizes.pdf")
graph_stats$ndates<-ndates1
plot(graph_stats$ndates,graph_stats$nodes/max(graph_stats$nodes),"l")
lines(Randindex$ndates,Randindex$V2,"l",col="blue")
dev.off()
