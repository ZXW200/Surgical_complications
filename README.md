Datasource

OpenML Dataset: ID 45648 — MIC (Myocardial infarction complications)




Use the following code to access four datasets separately：

HAS-POST=1 indicates that any complication field with POST has a value of 1 (such as SVT_POST, MP_TP_POST, K_SH-POST, P_POST, IBS-POST, GT-POST...)
Death_with_complication	Means LET_IS == 1 AND HAS_POST == 1	 Death+occurrence of at least one POST complication
Normal_death_no_complication	Meas LET_IS == 1 AND HAS_POST == 0	Death+no occurrence of POST complications
Alive_no_complication	means LET_IS == 0 AND HAS_POST == 0	Survival+no complications
Alive_with_complication	means LET_IS == 0 AND HAS_POST == 1	Survival+Complications

df[df["GROUP"] == "Death_with_complication"]
df[df["GROUP"] == "Normal_death_no_complication"]
df[df["GROUP"] == "Alive_no_complication"]
df[df["GROUP"] == "Alive_with_complication"]


