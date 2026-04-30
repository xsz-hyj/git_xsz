import pandas as pd

df = pd.read_excel(r"D:\论文\绿色金融指数构建\绿色金融指标变量\上市公司匹配green_bond.xlsx")

df.columns = df.columns.str.strip()

df["上市公司代码"] = (
    df["上市公司代码"]
    .astype(str)
    .str.replace(".0","", regex=False)
    .str.strip()
    .str.zfill(6)
)

df.to_csv(r"D:\论文\绿色金融指数构建\绿色金融指标变量\上市公司匹配green_bond.csv", index=False, encoding="utf-8-sig")

print("ok")