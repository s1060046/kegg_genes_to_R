# kegg_genes_to_R
Generating lists of genes in Kegg pathway for R

Python script takes Kegg pathway identifier (e.g. mmu04071) and generates a text file with all the Kegg genes from that pathway. attach_gene_name_kegg function in R script uses input from the text file and converts it into external gene names for downstream analysis in R.

## Python script

For the python script you will need requests and beautifulsoup4 installed in the environment and at least Python 3.8.5

Here is an example of the usage (python script needs to be in the working directory).

```{shell, echo = TRUE, eval = TRUE, collapse = TRUE}
python get_Kegg_gene.py mmu04071 Sphingolipid_signaling_pathway.txt
```

This will generate a txt file called "Sphingolipid_signaling_pathway.txt" with all the genes in mmu04071 Kegg pathway

## R function
For the R function you need readr, KEGGREST and stringr installed.

```{r, echo = TRUE, eval = TRUE, collapse = TRUE}

if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("KEGGREST")

install.packages("stringr")
install.packages("readr")


library("KEGGREST")
library("stringr")
library("readr")


```
load in dependencies and run the R script file "attach_gene_name_kegg.R" in RStudio. This will create a function called attach_gene_name_kegg. You can create an R data.frame with external gene names under gene_names column and the title of the Kegg pathway under Kegg which can be used in the downstream functional analysis. You will need the text file from the python script in the working directory

```{r, echo = TRUE, eval = TRUE, collapse = TRUE}

Sphingolipid_signaling_pathway <- attach_gene_name_kegg("Sphingolipid_signaling_pathway.txt", "Sphingolipid signaling pathway")

```