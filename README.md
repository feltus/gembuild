# This Workflow will prepare a series of normal (GTEX) and tunor (TCGA) co-normalized gene expression matrices from Wang et al GEMs (https://pubmed.ncbi.nlm.nih.gov/29664468/).  GEMs will be mixed and separated into train and test GEMs for AI/ML applications.

#Download GEMs
https://figshare.com/articles/dataset/Data_record_3/5330593

#Merge GEMs from Wang et al
python mergegem.py bladderrsemfpkmgtex.txt blcarsemfpkmtcgat.txt BLAD_BLCA.txt
python mergegem.py breastrsemfpkmgtex.txt brcarsemfpkmtcgat.txt BREA_BRCA.txt
python mergegem.py cervixrsemfpkmgtex.txt cescrsemfpkmtcgat.txt CERV_CESC.txt
python mergegem.py colonrsemfpkmgtex.txt coadrsemfpkmtcgat.txt COLO_COAD.txt
python mergegem.py esophagus_gasrsemfpkmgtex.txt escarsemfpkmtcgat.txt GASR_ESCA.txt
python mergegem.py esophagus_mucrsemfpkmgtex.txt escarsemfpkmtcgat.txt MUCR_ESCA.txt
python mergegem.py esophagus_musrsemfpkmgtex.txt escarsemfpkmtcgat.txt MUSR_ESCA.txt
python mergegem.py kidneyrsemfpkmgtex.txt kircrsemfpkmtcgat.txt KIDN_KIRC.txt
python mergegem.py kidneyrsemfpkmgtex.txt kirprsemfpkmtcgat.txt KIDN_KIRP.txt
python mergegem.py kidneyrsemfpkmgtex.txt kichrsemfpkmtcgat.txt KIDN_KICH.txt
python mergegem.py liverrsemfpkmgtex.txt lihcrsemfpkmtcgat.txt LIVE_LIHC.txt
python mergegem.py lungrsemfpkmgtex.txt luadrsemfpkmtcgat.txt LUNG_LUAD.txt
python mergegem.py lungrsemfpkmgtex.txt luscrsemfpkmtcgat.txt LUNG_LUSC.txt
python mergegem.py prostatersemfpkmgtex.txt pradrsemfpkmtcgat.txt PROS_PRAD.txt
python mergegem.py thyroidrsemfpkmgtex.txt thcarsemfpkmtcgat.txt THYR_THCR.txt
python mergegem.py uterusrsemfpkmgtex.txt ucecrsemfpkmtcgat.txt UTER_UCEC.txt
python mergegem.py uterusrsemfpkmgtex.txt ucsrsemfpkmtcgat.txt UTER_UCSR.txt
python mergegem.py stomachrsemfpkmgtex.txt stadrsemfpkmtcgat.txt STOM_STAD.txt



#Transpose the matrices/
bash transpose.sh COLO_COAD.txt > COLO_COAD_transpose.txt
bash transpose.sh ESOP_ESCA.txt> ESOP_ESCA_transpose.txt
bash transpose.sh KIDN_KIRC.txt> KIDN_KIRC_transpose.txt
bash transpose.sh KIDN_KIRP.txt> KIDN_KIRP_transpose.txt
bash transpose.sh BRES_BRCA.txt > BRES_BRCA_transpose.txt


bash ../PREPROCESS/transpose.sh LIVE_LIHC.txt> LIVE_LIHC_transpose.txt


# head BLAD_BLCA_train.txt | awk '{print $1,$2,$3}';  head COLO_COAD_transpose.txt | awk '{print $1,$2,$3}'


#Split GEMs into test and train sets
bash split_gem.sh COLO_COAD_transpose.txt COLO_COAD_train.txt COLO_COAD_test.txt
bash split_gem.sh ESOP_ESCA_transpose.txt ESOP_ESCA_train.txt ESOP_ESCA_test.txt
bash ../PREPROCESS/split_gem.sh KIDN_KIRC_transpose.txt KIDN_KIRC_train.txt KIDN_KIRC_test.txt
bash ../PREPROCESS/split_gem.sh KIDN_KIRP_transpose.txt KIDN_KIRP_train.txt KIDN_KIRP_test.txt
bash ../PREPROCESS/split_gem.sh LIVE_LIHC_transpose.txt KIDN_KIRP_train.txt LIVE_LIHC_test.txt


#Convert to tab-delimited and get rid of HUGO_SYMBOL
cat COLO_COAD_train.txt | awk '{$1=$1}1' OFS='\t'  > COLO_COAD.train
cat COLO_COAD_test.txt | awk '{$1=$1}1' OFS='\t'  > COLO_COAD.test
cat ESOP_ESCA_train.txt | awk '{$1=$1}1' OFS='\t'  > ESOP_ESCA.train
cat ESOP_ESCA_test.txt | awk '{$1=$1}1' OFS='\t'  > ESOP_ESCA.test
cat KIDN_KIRC_train.txt | awk '{$1=$1}1' OFS='\t'  > KIDN_KIRC.train
cat KIDN_KIRC_test.txt | awk '{$1=$1}1' OFS='\t'  > KIDN_KIRC.test
cat KIDN_KIRP_train.txt | awk '{$1=$1}1' OFS='\t'  > KIDN_KIRP.train
cat KIDN_KIRP_test.txt | awk '{$1=$1}1' OFS='\t'  > KIDN_KIRP.test


cat LIVE_LIHC_test.txt | awk '{$1=$1}1' OFS='\t'  > LIVE_LIHC.test
cat LIVE_LIHC_train.txt | awk '{$1=$1}1' OFS='\t'  > LIVE_LIHC.train


#make label files
bash make_label.sh COLO_COAD.train 
bash make_label.sh COLO_COAD.test
bash make_label.sh ESOP_ESCA.train 
bash make_label.sh ESOP_ESCA.test
bash ../PREPROCESS/make_label.sh KIDN_KIRC.train 
bash ../PREPROCESS/make_label.sh KIDN_KIRC.test
bash ../PREPROCESS/make_label.sh KIDN_KIRP.train
bash ../PREPROCESS/make_label.sh KIDN_KIRP.test


bash ../PREPROCESS/make_label.sh LIVE_LIHC.train
bash ../PREPROCESS/make_label.sh  LIVE_LIHC.test
