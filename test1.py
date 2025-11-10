from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff("Data.arff")

df = pd.DataFrame(data)

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ---- 定义并发症列 ----
post_cols = [c for c in ["SVT_POST", "MP_TP_POST", "K_SH_POST", "O_L_POST", "IBS_POST"] if c in df.columns]
has_post = (df[post_cols].fillna(0).max(axis=1) >= 1).astype(int)
df = df.copy()
# ---- 根据生存与并发症情况分组 ----
df["GROUP"] = ""
df.loc[(df["LET_IS"] == 1) & (has_post == 1), "GROUP"] = "Death_with_complication"
df.loc[(df["LET_IS"] == 1) & (has_post == 0), "GROUP"] = "Normal_death_no_complication"
df.loc[(df["LET_IS"] == 0) & (has_post == 0), "GROUP"] = "Alive_no_complication"
df.loc[(df["LET_IS"] == 0) & (has_post == 1), "GROUP"] = "Alive_with_complication"

# ---- 保存结果 ----
import os
os.makedirs("CleanedData", exist_ok=True)

# 导出完整数据和子集
df.to_csv("CleanedData/all_grouped.csv", index=False)

norm_death = df[df["GROUP"] == "Normal_death_no_complication"]
norm_death.to_csv("CleanedData/data_normal_death.csv", index=False)

complication_death = df[df["GROUP"] == "Death_with_complication"]
complication_death.to_csv("CleanedData/data_complication_death.csv", index=False)