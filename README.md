分析心肌梗死（MI）患者在是否发生 POST 并发症 与 是否死亡（LET_IS） 之间的关系，并将样本划分为四个临床分组便于后续建模与可视化。

1) 数据来源

OpenML Dataset: ID 45648 — MIC (Myocardial infarction complications)

格式: ARFF

备注: 名义（nominal）类型在 scipy.io.arff.loadarff 读入后常为 bytes（例如 b'1'），需转换为数值以便筛选与计算。

2) 分组规则（核心）

我们将每条记录划分为以下 四个互斥分组：

组名	条件（伪代码）	说明
Death_with_complication	LET_IS == 1 AND HAS_POST == 1	死亡 + 出现至少一个 POST 并发症
Normal_death_no_complication	LET_IS == 1 AND HAS_POST == 0	死亡 + 未出现 POST 并发症（你特别要求识别的“正常死亡”）
Alive_no_complication	LET_IS == 0 AND HAS_POST == 0	存活 + 无并发症
Alive_with_complication	LET_IS == 0 AND HAS_POST == 1	存活 + 有并发症

其中：

HAS_POST = 1 表示任一带 POST 的并发症字段取值为 1（如：SVT_POST, MP_TP_POST, K_SH_POST, O_L_POST, IBS_POST, GT_POST …）。

你可以自由扩展 POST 字段集合（见下文“可配置项”）。

3) 依赖环境
python >= 3.9
pandas
scipy    # 用于 scipy.io.arff


安装：

pip install pandas scipy
