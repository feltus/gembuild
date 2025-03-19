# This Workflow will prepare a series of normal (GTEX) and tunor (TCGA) co-normalized gene expression matrices (GEMs) from Wang et al (https://pubmed.ncbi.nlm.nih.gov/29664468/).  GEMs will be mixed and separated into train and test GEMs for AI/ML applications.

## Download GEMs
https://figshare.com/articles/dataset/Data_record_3/5330593

## Here is a subset of Normal-GTEX and Tumor-TCGA GEM files and the merged label.: Normal-GTEX and Tumor-TCGA (TCGA normal is not included).
```
bladder-rsem-fpkm-gtex.txt	BLADN
blca-rsem-fpkm-tcga-t.txt	BLCAT
blca-rsem-fpkm-tcga.txt	BLCAN
brca-rsem-fpkm-tcga-t.txt	BRCAT
brca-rsem-fpkm-tcga.txt	BRCAN
breast-rsem-fpkm-gtex.txt	BREAN
cervix-rsem-fpkm-gtex.txt	CERVN
cesc-rsem-fpkm-tcga-t.txt	CESCT
cesc-rsem-fpkm-tcga.txt	CESCN
chol-rsem-fpkm-tcga-t.txt	CHOLT
chol-rsem-fpkm-tcga.txt	CHOLN
coad-rsem-fpkm-tcga-t.txt	COADT
coad-rsem-fpkm-tcga.txt	COADN
colon-rsem-fpkm-gtex.txt	COLON
esca-rsem-fpkm-tcga-t.txt	ESCAT
esca-rsem-fpkm-tcga.txt	ESCAN
esophagus_gas-rsem-fpkm-gtex.txt	ESOGN
esophagus_muc-rsem-fpkm-gtex.txt	ESOCN
esophagus_mus-rsem-fpkm-gtex.txt	ESOSN
hnsc-rsem-fpkm-tcga-t.txt	HNSCT
hnsc-rsem-fpkm-tcga.txt	HNSCN
kich-rsem-fpkm-tcga-t.txt	KICHT
kich-rsem-fpkm-tcga.txt	KICHN
kidney-rsem-fpkm-gtex.txt	KIDNN
kirc-rsem-fpkm-tcga-t.txt	KIRCT
kirc-rsem-fpkm-tcga.txt	KIRCN
kirp-rsem-fpkm-tcga-t.txt	KIRPT
kirp-rsem-fpkm-tcga.txt	KIRPN
lihc-rsem-fpkm-tcga-t.txt	LIHCT
lihc-rsem-fpkm-tcga.txt	LIHCN
liver-rsem-fpkm-gtex.txt	LIVEN
luad-rsem-fpkm-tcga-t.txt	LUADT
luad-rsem-fpkm-tcga.txt	LUADN
lung-rsem-fpkm-gtex.txt	LUNGN
lusc-rsem-fpkm-tcga-t.txt	LUSCT
lusc-rsem-fpkm-tcga.txt	LUSCN
prad-rsem-fpkm-tcga-t.txt	PRADT
prad-rsem-fpkm-tcga.txt	PRADN
prostate-rsem-fpkm-gtex.txt	PROSN
read-rsem-fpkm-tcga-t.txt	READT
read-rsem-fpkm-tcga.txt	READN
salivary-rsem-fpkm-gtex.txt	SALIN
stad-rsem-fpkm-tcga-t.txt	STADT
stad-rsem-fpkm-tcga.txt	STADN
stomach-rsem-fpkm-gtex.txt	STOMN
thca-rsem-fpkm-tcga-t.txt	THCAT
thca-rsem-fpkm-tcga.txt	THCAN
thyroid-rsem-fpkm-gtex.txt	THYRN
ucec-rsem-fpkm-tcga-t.txt	UCECT
ucec-rsem-fpkm-tcga.txt	UCECN
ucs-rsem-fpkm-tcga-t.txt	UCST
uterus-rsem-fpkm-gtex.txt	UTERN
```

## Merge GEMs from Wang et al
```
python gembuild/gem_merge.py bladder-rsem-fpkm-gtex.txt blca-rsem-fpkm-tcga-t.txt BLADN_BLCAT.txt
python gembuild/gem_merge.py breast-rsem-fpkm-gtex.txt brca-rsem-fpkm-tcga-t.txt BREAN_BRCAT.txt
python gembuild/gem_merge.py cervix-rsem-fpkm-gtex.txt cesc-rsem-fpkm-tcga-t.txt CERVN_CESCT.txt
python gembuild/gem_merge.py colon-rsem-fpkm-gtex.txt coad-rsem-fpkm-tcga-t.txt COLON_COADT.txt
python gembuild/gem_merge.py esophagus_gas-rsem-fpkm-gtex.txt esca-rsem-fpkm-tcga-t.txt ESOGN_ESCAT.txt
python gembuild/gem_merge.py kidney-rsem-fpkm-gtex.txt kirc-rsem-fpkm-tcga-t.txt KIDNN_KIRCT.txt
python gembuild/gem_merge.py kidney-rsem-fpkm-gtex.txt kirp-rsem-fpkm-tcga-t.txt KIDNN_KIRPT.txt
python gembuild/gem_merge.py liver-rsem-fpkm-gtex.txt lihc-rsem-fpkm-tcga-t.txt LIVEN_LIHCT.txt
python gembuild/gem_merge.py prostate-rsem-fpkm-gtex.txt prad-rsem-fpkm-tcga-t.txt PROSN_PRADT.txt
python gembuild/gem_merge.py stomach-rsem-fpkm-gtex.txt stad-rsem-fpkm-tcga-t.txt STOMN_STADT.txt
python gembuild/gem_merge.py thyroid-rsem-fpkm-gtex.txt thca-rsem-fpkm-tcga-t.txt THYRN_THCAT.txt
python gembuild/gem_merge.py lung-rsem-fpkm-gtex.txt luad-rsem-fpkm-tcga-t.txt LUNGN_LUADT.txt
python gembuild/gem_merge.py lung-rsem-fpkm-gtex.txt lusc-rsem-fpkm-tcga-t.txt LUNGN_LUSCT.txt
python gembuild/gem_merge.py uterus-rsem-fpkm-gtex.txt ucec-rsem-fpkm-tcga-t.txt UTERN_UCECT.txt
```

## Transpose the GEMs
```
bash gembuild/transpose_gem.sh BLADN_BLCAT.txt > BLADN_BLCAT_transpose.txt
bash gembuild/transpose_gem.sh BREAN_BRCAT.txt > BREAN_BRCAT_transpose.txt
bash gembuild/transpose_gem.sh CERVN_CESCT.txt > CERVN_CESCT_transpose.txt
bash gembuild/transpose_gem.sh COLON_COADT.txt > COLON_COADT_transpose.txt
bash gembuild/transpose_gem.sh ESOGN_ESCAT.txt > ESOGN_ESCAT_transpose.txt
bash gembuild/transpose_gem.sh KIDNN_KIRCT.txt > KIDNN_KIRCT_transpose.txt
bash gembuild/transpose_gem.sh KIDNN_KIRPT.txt > KIDNN_KIRPT_transpose.txt
bash gembuild/transpose_gem.sh LIVEN_LIHCT.txt > LIVEN_LIHCT_transpose.txt
bash gembuild/transpose_gem.sh PROSN_PRADT.txt > PROSN_PRADT_transpose.txt
bash gembuild/transpose_gem.sh STOMN_STADT.txt > STOMN_STADT_transpose.txt
bash gembuild/transpose_gem.sh THYRN_THCAT.txt > THYRN_THCAT_transpose.txt
bash gembuild/transpose_gem.sh LUNGN_LUADT.txt > LUNGN_LUADT_transpose.txt
bash gembuild/transpose_gem.sh LUNGN_LUSCT.txt > LUNGN_LUSCT_transpose.txt
bash gembuild/transpose_gem.sh UTERN_UCECT.txt > UTERN_UCECT_transpose.txt
```

## Split GEMs into test and train sets
```
bash gembuild/split_gem.sh BLADN_BLCAT_transpose.txt BLADN_BLCAT_train.txt BLADN_BLCAT_test.txt
bash gembuild/split_gem.sh BREAN_BRCAT_transpose.txt BREAN_BRCAT_train.txt BREAN_BRCAT_test.txt
bash gembuild/split_gem.sh CERVN_CESCT_transpose.txt CERVN_CESCT_train.txt CERVN_CESCT_test.txt
bash gembuild/split_gem.sh COLON_COADT_transpose.txt COLON_COADT_train.txt COLON_COADT_test.txt
bash gembuild/split_gem.sh ESOGN_ESCAT_transpose.txt ESOGN_ESCAT_train.txt ESOGN_ESCAT_test.txt
bash gembuild/split_gem.sh KIDNN_KIRCT_transpose.txt KIDNN_KIRCT_train.txt KIDNN_KIRCT_test.txt
bash gembuild/split_gem.sh KIDNN_KIRPT_transpose.txt KIDNN_KIRPT_train.txt KIDNN_KIRPT_test.txt
bash gembuild/split_gem.sh LIVEN_LIHCT_transpose.txt LIVEN_LIHCT_train.txt LIVEN_LIHCT_test.txt
bash gembuild/split_gem.sh PROSN_PRADT_transpose.txt PROSN_PRADT_train.txt PROSN_PRADT_test.txt
bash gembuild/split_gem.sh STOMN_STADT_transpose.txt STOMN_STADT_train.txt STOMN_STADT_test.txt
bash gembuild/split_gem.sh THYRN_THCAT_transpose.txt THYRN_THCAT_train.txt THYRN_THCAT_test.txt
bash gembuild/split_gem.sh LUNGN_LUADT_transpose.txt LUNGN_LUADT_train.txt LUNGN_LUADT_test.txt
bash gembuild/split_gem.sh LUNGN_LUSCT_transpose.txt LUNGN_LUSCT_train.txt LUNGN_LUSCT_test.txt
bash gembuild/split_gem.sh UTERN_UCECT_transpose.txt UTERN_UCECT_train.txt UTERN_UCECT_test.txt
```

## Convert GEMS to tab-delimited format
```
cat BLADN_BLCAT_train.txt | awk '{$1=$1}1' OFS='\t'  > BLADN_BLCAT.train; cat BLADN_BLCAT_test.txt | awk '{$1=$1}1' OFS='\t'  > BLADN_BLCAT.test
cat BREAN_BRCAT_train.txt | awk '{$1=$1}1' OFS='\t'  > BREAN_BRCAT.train; cat BREAN_BRCAT_test.txt | awk '{$1=$1}1' OFS='\t'  > BREAN_BRCAT.test
cat CERVN_CESCT_train.txt | awk '{$1=$1}1' OFS='\t'  > CERVN_CESCT.train; cat CERVN_CESCT_test.txt | awk '{$1=$1}1' OFS='\t'  > CERVN_CESCT.test
cat COLON_COADT_train.txt | awk '{$1=$1}1' OFS='\t'  > COLON_COADT.train; cat COLON_COADT_test.txt | awk '{$1=$1}1' OFS='\t'  > COLON_COADT.test
cat ESOGN_ESCAT_train.txt | awk '{$1=$1}1' OFS='\t'  > ESOGN_ESCAT.train; cat ESOGN_ESCAT_test.txt | awk '{$1=$1}1' OFS='\t'  > ESOGN_ESCAT.test
cat KIDNN_KIRCT_train.txt | awk '{$1=$1}1' OFS='\t'  > KIDNN_KIRCT.train; cat KIDNN_KIRCT_test.txt | awk '{$1=$1}1' OFS='\t'  > KIDNN_KIRCT.test
cat KIDNN_KIRPT_train.txt | awk '{$1=$1}1' OFS='\t'  > KIDNN_KIRPT.train; cat KIDNN_KIRPT_test.txt | awk '{$1=$1}1' OFS='\t'  > KIDNN_KIRPT.test
cat LIVEN_LIHCT_train.txt | awk '{$1=$1}1' OFS='\t'  > LIVEN_LIHCT.train; cat LIVEN_LIHCT_test.txt | awk '{$1=$1}1' OFS='\t'  > LIVEN_LIHCT.test
cat PROSN_PRADT_train.txt | awk '{$1=$1}1' OFS='\t'  > PROSN_PRADT.train; cat PROSN_PRADT_test.txt | awk '{$1=$1}1' OFS='\t'  > PROSN_PRADT.test
cat STOMN_STADT_train.txt | awk '{$1=$1}1' OFS='\t'  > STOMN_STADT.train; cat STOMN_STADT_test.txt | awk '{$1=$1}1' OFS='\t'  > STOMN_STADT.test
cat THYRN_THCAT_train.txt | awk '{$1=$1}1' OFS='\t'  > THYRN_THCAT.train; cat THYRN_THCAT_test.txt | awk '{$1=$1}1' OFS='\t'  > THYRN_THCAT.test
cat LUNGN_LUADT_train.txt | awk '{$1=$1}1' OFS='\t'  > LUNGN_LUADT.train; cat LUNGN_LUADT_test.txt | awk '{$1=$1}1' OFS='\t'  > LUNGN_LUADT.test
cat LUNGN_LUSCT_train.txt | awk '{$1=$1}1' OFS='\t'  > LUNGN_LUSCT.train; cat LUNGN_LUSCT_test.txt | awk '{$1=$1}1' OFS='\t'  > LUNGN_LUSCT.test
cat UTERN_UCECT_train.txt | awk '{$1=$1}1' OFS='\t'  > UTERN_UCECT.train; cat UTERN_UCECT_test.txt | awk '{$1=$1}1' OFS='\t'  > UTERN_UCECT.test
```


## Make  group label files (e.g. TUMOR, NORMAL)
```
bash gembuild/make_labels.sh BLADN_BLCAT.train; bash gembuild/make_labels.sh BLADN_BLCAT.test
bash gembuild/make_labels.sh BREAN_BRCAT.train; bash gembuild/make_labels.sh BREAN_BRCAT.test
bash gembuild/make_labels.sh CERVN_CESCT.train; bash gembuild/make_labels.sh CERVN_CESCT.test
bash gembuild/make_labels.sh COLON_COADT.train; bash gembuild/make_labels.sh COLON_COADT.test
bash gembuild/make_labels.sh ESOGN_ESCAT.train; bash gembuild/make_labels.sh ESOGN_ESCAT.test
bash gembuild/make_labels.sh KIDNN_KIRCT.train; bash gembuild/make_labels.sh KIDNN_KIRCT.test
bash gembuild/make_labels.sh KIDNN_KIRPT.train; bash gembuild/make_labels.sh KIDNN_KIRPT.test
bash gembuild/make_labels.sh LIVEN_LIHCT.train; bash gembuild/make_labels.sh LIVEN_LIHCT.test
bash gembuild/make_labels.sh PROSN_PRADT.train; bash gembuild/make_labels.sh PROSN_PRADT.test
bash gembuild/make_labels.sh STOMN_STADT.train; bash gembuild/make_labels.sh STOMN_STADT.test
bash gembuild/make_labels.sh THYRN_THCAT.train; bash gembuild/make_labels.sh THYRN_THCAT.test
bash gembuild/make_labels.sh LUNGN_LUADT.train; bash gembuild/make_labels.sh LUNGN_LUADT.test
bash gembuild/make_labels.sh LUNGN_LUSCT.train; bash gembuild/make_labels.sh LUNGN_LUSCT.test
bash gembuild/make_labels.sh UTERN_UCECT.train; bash gembuild/make_labels.sh UTERN_UCECT.test
```

## Draw a histogram of all GEMs
```
for i in *.train; do for k in *.txt; do python GEM_histogram.py -e $i -g $k -o $i.$k.png; done; done
for i in *.test; do for k in *.txt; do python GEM_histogram.py -e $i -g $k -o $i.$k.png; done; done
```
