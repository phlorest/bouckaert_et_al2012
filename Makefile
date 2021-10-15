

all: summary.trees posterior.trees data.nex

summary.trees: original/1219669IndoEuropean_2MCCtrees_annotated.tre
	nexus trees -t -c -d 2 $< $@

posterior.trees: original/IE2011_RelaxedCovarion_AllSingletonsGeo_Combined.trees.gz
	# remove 1000 (10%), sample 1000
	nexus trees -c -d 1-1000 $< -o tmp
	nexus trees -n 1000 tmp -o $@
	rm tmp

data.nex:
	cp original/IELex_Bouckaert2012.nex $@
