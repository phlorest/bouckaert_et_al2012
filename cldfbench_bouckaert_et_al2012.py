import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "bouckaert_et_al2012"

    def cmd_makecldf(self, args):
        self.init(args)

        summary = self.raw_dir.read_tree(
            '1219669IndoEuropean_2MCCtrees_annotated.tre')
        args.writer.add_summary(summary, self.metadata, args.log)

        posterior = self.raw_dir.read_trees(
            'IE2011_RelaxedCovarion_AllSingletonsGeo_Combined.trees.gz',
            burnin=1000, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)
        
        args.writer.add_data(
            self.raw_dir.read_nexus('IELex_Bouckaert2012.nex'),
            self.characters,
            args.log)
