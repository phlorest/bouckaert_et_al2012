# Notes

These are the corrected trees published in
http://science.sciencemag.org/content/342/6165/1446.1


Reanalysed beast analyses in ./reanalysis-SJG2015



## Data:

> We recorded word forms and cognacy judgments across 207 meanings in 103 contemporary and ancient languages.

> Cognate data were coded as binary characters showing the presence or ab- sence of a cognate set in a language. There
> were 5047 cognate sets in total, with most meanings represented by several different cognate sets. All cognate coding
> decisions were checked with published historical linguistic sources (Table S1). The database contained 25908 cognate
> coded lexemes. Of these, 67% came originally from ref. (17), 14% from ref. (16), and 19% were newly compiled from
> published sources. Ref. (17 ) required considerable correction, and changes were made to approximately 26% of coding
> decisions on individual lexemes. Ref. (16) required corrections to only 0.5% of lexemes.


## Methods:

| Model                                | Score       | Program  | Comment            |
|--------------------------------------|-------------|----------|                    |
| CTMC + strict clock                  |-53355 ± 0.2 | BEAST2   |                    |
| CTMC + relaxed clock                 |-53017 ± 0.9 | BEAST2   |                    |
| Covarion + strict clock              |-52411 ± 0.2 | BEAST2   |                    |
| Covarion + relaxed clock             |-52061 ± 0.2 | BEAST2   | best fitting       |
| Stochastic Dollo + strict clock      |-51954 ± 0.2 | BEAST2   |                    |
| Stochastic Dollo + relaxed clock     |-51530 ± 0.5 | BEAST2   |                    |
| Phylogeography - RRW                 |             | BEAST2   |                    |
| Phylogeography - Brownian            |             | BEAST2   |                    |



## Analysis:


