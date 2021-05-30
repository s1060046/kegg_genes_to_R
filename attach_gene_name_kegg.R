attach_gene_name_kegg <- 
function(directory, title){
  dat = read_table2(directory, col_names = FALSE)
  dat$gene_name <- apply(dat, 1,function(x){unlist(keggGet(x[1])[[1]]["NAME"])})
  dat$gene_names <- apply(dat, 1, function(x){str_split(x["gene_name"], "\\,")[[1]][1]})
  dat <- data.frame(gene_names = dat$gene_names, Kegg = title)
  
  return(dat)
}