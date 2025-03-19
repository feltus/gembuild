# This Workflow will prepare a series of normal (GTEX) and tunor (TCGA) co-normalized gene expression matrices from Wang et al GEMs (https://pubmed.ncbi.nlm.nih.gov/29664468/).  GEMs will be mixed and separated into train and test GEMs for AI/ML applications.

## Download GEMs
https://figshare.com/articles/dataset/Data_record_3/5330593

## Here is a subset of GEMS: Normal-GTEX and Tumor-TCGA (TCGA normal is not included).
GEMA	GEMB	GEM_MERGE
bladderrsemfpkmgtex.txt	blcarsemfpkmtcgat.txt	BLAD_BLCA
breastrsemfpkmgtex.txt	brcarsemfpkmtcgat.txt	BREA_BRCA
cervixrsemfpkmgtex.txt	cescrsemfpkmtcgat.txt	CERV_CESC
colonrsemfpkmgtex.txt	coadrsemfpkmtcgat.txt	COLO_COAD
esophagus_gasrsemfpkmgtex.txt	escarsemfpkmtcgat.txt	GASR_ESCA
esophagus_mucrsemfpkmgtex.txt	escarsemfpkmtcgat.txt	MUCR_ESCA
esophagus_musrsemfpkmgtex.txt	escarsemfpkmtcgat.txt	MUSR_ESCA
kidneyrsemfpkmgtex.txt	kircrsemfpkmtcgat.txt	KIDN_KIRC
kidneyrsemfpkmgtex.txt	kirprsemfpkmtcgat.txt	KIDN_KIRP
kidneyrsemfpkmgtex.txt	kichrsemfpkmtcgat.txt	KIDN_KICH
liverrsemfpkmgtex.txt	lihcrsemfpkmtcgat.txt	LIVE_LIHC
lungrsemfpkmgtex.txt	luadrsemfpkmtcgat.txt	LUNG_LUAD
lungrsemfpkmgtex.txt	luscrsemfpkmtcgat.txt	LUNG_LUSC
prostatersemfpkmgtex.txt	pradrsemfpkmtcgat.txt	PROS_PRAD
thyroidrsemfpkmgtex.txt	thcarsemfpkmtcgat.txt	THYR_THCR
uterusrsemfpkmgtex.txt	ucecrsemfpkmtcgat.txt	UTER_UCEC
uterusrsemfpkmgtex.txt	ucsrsemfpkmtcgat.txt	UTER_UCSR
stomachrsemfpkmgtex.txt	stadrsemfpkmtcgat.txt	STOM_STAD

## Merge GEMs from Wang et al
```
python gem_merge.py bladderrsemfpkmgtex.txt blcarsemfpkmtcgat.txt BLAD_BLCA.txt
python gem_merge.py breastrsemfpkmgtex.txt brcarsemfpkmtcgat.txt BREA_BRCA.txt
python gem_merge.py cervixrsemfpkmgtex.txt cescrsemfpkmtcgat.txt CERV_CESC.txt
python gem_merge.py colonrsemfpkmgtex.txt coadrsemfpkmtcgat.txt COLO_COAD.txt
python gem_merge.py esophagus_gasrsemfpkmgtex.txt escarsemfpkmtcgat.txt GASR_ESCA.txt
python gem_merge.py esophagus_mucrsemfpkmgtex.txt escarsemfpkmtcgat.txt MUCR_ESCA.txt
python gem_merge.py esophagus_musrsemfpkmgtex.txt escarsemfpkmtcgat.txt MUSR_ESCA.txt
python gem_merge.py kidneyrsemfpkmgtex.txt kircrsemfpkmtcgat.txt KIDN_KIRC.txt
python gem_merge.py kidneyrsemfpkmgtex.txt kirprsemfpkmtcgat.txt KIDN_KIRP.txt
python gem_merge.py kidneyrsemfpkmgtex.txt kichrsemfpkmtcgat.txt KIDN_KICH.txt
python gem_merge.py liverrsemfpkmgtex.txt lihcrsemfpkmtcgat.txt LIVE_LIHC.txt
python gem_merge.py lungrsemfpkmgtex.txt luadrsemfpkmtcgat.txt LUNG_LUAD.txt
python gem_merge.py lungrsemfpkmgtex.txt luscrsemfpkmtcgat.txt LUNG_LUSC.txt
python gem_merge.py prostatersemfpkmgtex.txt pradrsemfpkmtcgat.txt PROS_PRAD.txt
python gem_merge.py thyroidrsemfpkmgtex.txt thcarsemfpkmtcgat.txt THYR_THCR.txt
python gem_merge.py uterusrsemfpkmgtex.txt ucecrsemfpkmtcgat.txt UTER_UCEC.txt
python gem_merge.py uterusrsemfpkmgtex.txt ucsrsemfpkmtcgat.txt UTER_UCSR.txt
python gem_merge.py stomachrsemfpkmgtex.txt stadrsemfpkmtcgat.txt STOM_STAD.txt
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
bash make_label.sh BREA_BRCA.train; bash make_label.sh BREA_BRCA.test"
bash make_label.sh CERV_CESC.train; bash make_label.sh CERV_CESC.test"
bash make_label.sh COLO_COAD.train; bash make_label.sh COLO_COAD.test"
bash make_label.sh GASR_ESCA.train; bash make_label.sh GASR_ESCA.test"
bash make_label.sh MUCR_ESCA.train; bash make_label.sh MUCR_ESCA.test"
bash make_label.sh MUSR_ESCA.train; bash make_label.sh MUSR_ESCA.test"
bash make_label.sh KIDN_KIRC.train; bash make_label.sh KIDN_KIRC.test"
bash make_label.sh KIDN_KIRP.train; bash make_label.sh KIDN_KIRP.test"
bash make_label.sh KIDN_KICH.train; bash make_label.sh KIDN_KICH.test"
bash make_label.sh LIVE_LIHC.train; bash make_label.sh LIVE_LIHC.test"
bash make_label.sh LUNG_LUAD.train; bash make_label.sh LUNG_LUAD.test"
bash make_label.sh LUNG_LUSC.train; bash make_label.sh LUNG_LUSC.test"
bash make_label.sh PROS_PRAD.train; bash make_label.sh PROS_PRAD.test"
bash make_label.sh THYR_THCR.train; bash make_label.sh THYR_THCR.test"
bash make_label.sh UTER_UCEC.train; bash make_label.sh UTER_UCEC.test"
bash make_label.sh UTER_UCSR.train; bash make_label.sh UTER_UCSR.test"
bash make_label.sh STOM_STAD.train; bash make_label.sh STOM_STAD.test"
```

## Draw a histogram of all GEMs
```
for i in *.train; do for k in *.txt; do python GEM_histogram.py -e $i -g $k -o $i.$k.png; done; done
for i in *.test; do for k in *.txt; do python GEM_histogram.py -e $i -g $k -o $i.$k.png; done; done
```
