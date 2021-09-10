

# -*- coding: utf-8 -*-
import json
import pandas as pd


columns_json_str = '{"M of H3O_p__1H3-16O_p__eXeL":"M","I":"I","S":"S","A":"A","gm_a":"gm_a","gm_s":"gm_s","E_f":"E_f","n_a":"n_a","dt_a":"dt_a","V_i":"V_i","V_f":"V_f","Q_i":"Q_i","Q_f":"Q_f","Ierr":"Ierr","Iref":"Iref","*":"*","g_i":"g_i","g_f":"g_f"}'
columns_dict = json.loads(columns_json_str)

dataset = pd.read_csv('H3O_p__1H3-16O_p__eXeL.csv', header=0, encoding='utf-8', dtype=str)
df = pd.DataFrame(dataset, columns=columns_dict.keys())


df.rename(columns=columns_dict, inplace=True) 



filepath = 'H3O_p__1H3-16O_p__eXeL.csv'
df_columns = pd.DataFrame([list(df.columns)])
df_columns.to_csv(filepath, mode='w', header=False, index=0) 

df.to_csv(filepath, mode='a', header=False, index=0)