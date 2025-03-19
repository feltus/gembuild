# This Workflow will prepare a series of normal (GTEX) and tunor (TCGA) co-normalized gene expression matrices (GEMs) from Wang et al (https://pubmed.ncbi.nlm.nih.gov/29664468/).  GEMs will be mixed and separated into train and test GEMs for AI/ML applications.

## Download GEMs
https://figshare.com/articles/dataset/Data_record_3/5330593

## Here is a subset of Normal-GTEX and Tumor-TCGA GEM files and the merged label.: Normal-GTEX and Tumor-TCGA (TCGA normal is not included).
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
python gem_merge.py bladder-rsem-fpkm-gtex.txt blca-rsem-fpkm-tcga-t.txt BLADN_BLCAT.txt
python gem_merge.py breast-rsem-fpkm-gtex.txt brca-rsem-fpkm-tcga-t.txt BREAN_BRCAT.txt
python gem_merge.py cervix-rsem-fpkm-gtex.txt cesc-rsem-fpkm-tcga-t.txt CERVN_CESCT.txt
python gem_merge.py colon-rsem-fpkm-gtex.txt coad-rsem-fpkm-tcga-t.txt COLON_COADT.txt
python gem_merge.py esophagus_gas-rsem-fpkm-gtex.txt esca-rsem-fpkm-tcga-t.txt ESOGN_ESCAT.txt
python gem_merge.py kidney-rsem-fpkm-gtex.txt kirc-rsem-fpkm-tcga-t.txt KIDNN_KIRCT.txt
python gem_merge.py kidney-rsem-fpkm-gtex.txt kirp-rsem-fpkm-tcga-t.txt KIDNN_KIRPT.txt
python gem_merge.py liver-rsem-fpkm-gtex.txt lihc-rsem-fpkm-tcga-t.txt LIVEN_LIHCT.txt
python gem_merge.py prostate-rsem-fpkm-gtex.txt prad-rsem-fpkm-tcga-t.txt PROSN_PRADT.txt
python gem_merge.py stomach-rsem-fpkm-gtex.txt stad-rsem-fpkm-tcga-t.txt STOMN_STADT.txt
python gem_merge.py thyroid-rsem-fpkm-gtex.txt thca-rsem-fpkm-tcga-t.txt THYRN_THCAT.txt
python gem_merge.py lung-rsem-fpkm-gtex.txt luad-rsem-fpkm-tcga-t.txt LUNGN_LUADT.txt
python gem_merge.py lung-rsem-fpkm-gtex.txt lusc-rsem-fpkm-tcga-t.txt LUNGN_LUSCT.txt
python gem_merge.py uterus-rsem-fpkm-gtex.txt ucec-rsem-fpkm-tcga-t.txt UTERN_UCECT.txt
```

## Transpose the GEMs
```
bash transpose_gem.sh BLAD_BLCA.txt > BLAD_BLCA_transpose.txt
bash transpose_gem.sh BREA_BRCA.txt > BREA_BRCA_transpose.txt
bash transpose_gem.sh CERV_CESC.txt > CERV_CESC_transpose.txt
bash transpose_gem.sh COLO_COAD.txt > COLO_COAD_transpose.txt
bash transpose_gem.sh GASR_ESCA.txt > GASR_ESCA_transpose.txt
bash transpose_gem.sh MUCR_ESCA.txt > MUCR_ESCA_transpose.txt
bash transpose_gem.sh MUSR_ESCA.txt > MUSR_ESCA_transpose.txt
bash transpose_gem.sh KIDN_KIRC.txt > KIDN_KIRC_transpose.txt
bash transpose_gem.sh KIDN_KIRP.txt > KIDN_KIRP_transpose.txt
bash transpose_gem.sh KIDN_KICH.txt > KIDN_KICH_transpose.txt
bash transpose_gem.sh LIVE_LIHC.txt > LIVE_LIHC_transpose.txt
bash transpose_gem.sh LUNG_LUAD.txt > LUNG_LUAD_transpose.txt
bash transpose_gem.sh LUNG_LUSC.txt > LUNG_LUSC_transpose.txt
bash transpose_gem.sh PROS_PRAD.txt > PROS_PRAD_transpose.txt
bash transpose_gem.sh THYR_THCR.txt > THYR_THCR_transpose.txt
bash transpose_gem.sh UTER_UCEC.txt > UTER_UCEC_transpose.txt
bash transpose_gem.sh UTER_UCSR.txt > UTER_UCSR_transpose.txt
bash transpose_gem.sh STOM_STAD.txt > STOM_STAD_transpose.txt
```

## Split GEMs into test and train sets
```
split_gem.sh BLAD_BLCA_transpose.txt BLAD_BLCA_train.txt BLAD_BLCA_test.txt
split_gem.sh BREA_BRCA_transpose.txt BREA_BRCA_train.txt BREA_BRCA_test.txt
split_gem.sh CERV_CESC_transpose.txt CERV_CESC_train.txt CERV_CESC_test.txt
split_gem.sh COLO_COAD_transpose.txt COLO_COAD_train.txt COLO_COAD_test.txt
split_gem.sh GASR_ESCA_transpose.txt GASR_ESCA_train.txt GASR_ESCA_test.txt
split_gem.sh MUCR_ESCA_transpose.txt MUCR_ESCA_train.txt MUCR_ESCA_test.txt
split_gem.sh MUSR_ESCA_transpose.txt MUSR_ESCA_train.txt MUSR_ESCA_test.txt
split_gem.sh KIDN_KIRC_transpose.txt KIDN_KIRC_train.txt KIDN_KIRC_test.txt
split_gem.sh KIDN_KIRP_transpose.txt KIDN_KIRP_train.txt KIDN_KIRP_test.txt
split_gem.sh KIDN_KICH_transpose.txt KIDN_KICH_train.txt KIDN_KICH_test.txt
split_gem.sh LIVE_LIHC_transpose.txt LIVE_LIHC_train.txt LIVE_LIHC_test.txt
split_gem.sh LUNG_LUAD_transpose.txt LUNG_LUAD_train.txt LUNG_LUAD_test.txt
split_gem.sh LUNG_LUSC_transpose.txt LUNG_LUSC_train.txt LUNG_LUSC_test.txt
split_gem.sh PROS_PRAD_transpose.txt PROS_PRAD_train.txt PROS_PRAD_test.txt
split_gem.sh THYR_THCR_transpose.txt THYR_THCR_train.txt THYR_THCR_test.txt
split_gem.sh UTER_UCEC_transpose.txt UTER_UCEC_train.txt UTER_UCEC_test.txt
split_gem.sh UTER_UCSR_transpose.txt UTER_UCSR_train.txt UTER_UCSR_test.txt
split_gem.sh STOM_STAD_transpose.txt STOM_STAD_train.txt STOM_STAD_test.txt
```

## Convert GEMS to tab-delimited format
```
cat BLAD_BLCA_train.txt | awk '{$1=$1}1' OFS='\t'  > BLAD_BLCA.train
cat BREA_BRCA_train.txt | awk '{$1=$1}1' OFS='\t'  > BREA_BRCA.train
cat CERV_CESC_train.txt | awk '{$1=$1}1' OFS='\t'  > CERV_CESC.train
cat COLO_COAD_train.txt | awk '{$1=$1}1' OFS='\t'  > COLO_COAD.train
cat GASR_ESCA_train.txt | awk '{$1=$1}1' OFS='\t'  > GASR_ESCA.train
cat MUCR_ESCA_train.txt | awk '{$1=$1}1' OFS='\t'  > MUCR_ESCA.train
cat MUSR_ESCA_train.txt | awk '{$1=$1}1' OFS='\t'  > MUSR_ESCA.train
cat KIDN_KIRC_train.txt | awk '{$1=$1}1' OFS='\t'  > KIDN_KIRC.train
cat KIDN_KIRP_train.txt | awk '{$1=$1}1' OFS='\t'  > KIDN_KIRP.train
cat KIDN_KICH_train.txt | awk '{$1=$1}1' OFS='\t'  > KIDN_KICH.train
cat LIVE_LIHC_train.txt | awk '{$1=$1}1' OFS='\t'  > LIVE_LIHC.train
cat LUNG_LUAD_train.txt | awk '{$1=$1}1' OFS='\t'  > LUNG_LUAD.train
cat LUNG_LUSC_train.txt | awk '{$1=$1}1' OFS='\t'  > LUNG_LUSC.train
cat PROS_PRAD_train.txt | awk '{$1=$1}1' OFS='\t'  > PROS_PRAD.train
cat THYR_THCR_train.txt | awk '{$1=$1}1' OFS='\t'  > THYR_THCR.train
cat UTER_UCEC_train.txt | awk '{$1=$1}1' OFS='\t'  > UTER_UCEC.train
cat UTER_UCSR_train.txt | awk '{$1=$1}1' OFS='\t'  > UTER_UCSR.train
cat STOM_STAD_train.txt | awk '{$1=$1}1' OFS='\t'  > STOM_STAD.train
```


## Make  group label files (e.g. TUMOR, NORMAL)
```bash make_label.sh BLAD_BLCA.train; bash make_label.sh BLAD_BLCA.test"
bash make_labels.sh BLAD_BLCA.train; bash make_labels.sh BLAD_BLCA.test"
bash make_labels.sh BREA_BRCA.train; bash make_labels.sh BREA_BRCA.test"
bash make_labels.sh CERV_CESC.train; bash make_labels.sh CERV_CESC.test"
bash make_labels.sh COLO_COAD.train; bash make_labels.sh COLO_COAD.test"
bash make_labels.sh GASR_ESCA.train; bash make_labels.sh GASR_ESCA.test"
bash make_labels.sh MUCR_ESCA.train; bash make_labels.sh MUCR_ESCA.test"
bash make_labels.sh MUSR_ESCA.train; bash make_labels.sh MUSR_ESCA.test"
bash make_labels.sh KIDN_KIRC.train; bash make_labels.sh KIDN_KIRC.test"
bash make_labels.sh KIDN_KIRP.train; bash make_labels.sh KIDN_KIRP.test"
bash make_labels.sh KIDN_KICH.train; bash make_labels.sh KIDN_KICH.test"
bash make_labels.sh LIVE_LIHC.train; bash make_labels.sh LIVE_LIHC.test"
bash make_labels.sh LUNG_LUAD.train; bash make_labels.sh LUNG_LUAD.test"
bash make_labels.sh LUNG_LUSC.train; bash make_labels.sh LUNG_LUSC.test"
bash make_labels.sh PROS_PRAD.train; bash make_labels.sh PROS_PRAD.test"
bash make_labels.sh THYR_THCR.train; bash make_labels.sh THYR_THCR.test"
bash make_labels.sh UTER_UCEC.train; bash make_labels.sh UTER_UCEC.test"
bash make_labels.sh UTER_UCSR.train; bash make_labels.sh UTER_UCSR.test"
bash make_labels.sh STOM_STAD.train; bash make_labels.sh STOM_STAD.test"
```

## Draw a histogram of all GEMs
```
for i in *.train; do for k in *.txt; do python GEM_histogram.py -e $i -g $k -o $i.$k.png; done; done
for i in *.test; do for k in *.txt; do python GEM_histogram.py -e $i -g $k -o $i.$k.png; done; done
```
