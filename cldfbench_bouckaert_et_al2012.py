import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "bouckaert_et_al2012"

    def cmd_makecldf(self, args):
        self.init(args)

        args.writer.add_summary(
                self.raw_dir.read_tree('1219669IndoEuropean_2MCCtrees_annotated.tre'),
                self.metadata,
                args.log)

        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('IE2011_RelaxedCovarion_AllSingletonsGeo_Combined.trees.gz'),
                1000),
            detranslate=True,
            as_nexus=True)

        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('IELex_Bouckaert2012.nex'),
            self.characters,
            args.log)
