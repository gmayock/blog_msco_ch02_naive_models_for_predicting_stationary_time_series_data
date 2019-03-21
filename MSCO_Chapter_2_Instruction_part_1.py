import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('filepath/chapter_2_instruction.xlsx', sheet_name='2.3.1_table_2.1', header=None, index_col=0).T
df.reset_index(drop=True, inplace=True)
print(df)

# # This is the simple scatter plot
plt.ylabel('Widget Demand (000s)');
plt.ylim(0,15);
plt.axes().yaxis.grid(linestyle=':');
plt.xlabel('Week');
plt.xlim(0,15);
plt.scatter(df['Week'], df['Demand']);
plt.title('Widget Demand Data');
# plt.show();


# This plots the arithmetic mean model
plt.plot(df['Week'], df['Demand']);
plt.plot(df['Week'], [df['Demand'].mean() for i in df['Demand']], marker='$.$')
plt.show();

# This plots the last period value model
plt.plot(df['Week'], df['Demand']);
plt.plot(df['Week'][1:], df['Demand'][:-1], marker='$.$')
plt.show();

# This code adds the arithmetic mean predictions
df['a_m_pred'] = [int(df['Demand'].mean()) for i in df['Demand']]
df['l_p_v_pred'] = 0
df['l_p_v_pred'][1:] = df['Demand'][:-1]
df = df[1:]

# This code calculates the abs and sq errors
df['a_m_abs_err'] = abs(df['Demand']-df['a_m_pred'])
df['a_m_sq_err'] = pow(df['Demand']-df['a_m_pred'],2)
df['l_p_v_abs_err'] = abs(df['Demand']-df['l_p_v_pred'])
df['l_p_v_sq_err'] = (df['Demand']-df['l_p_v_pred'])**2
# print(df, "\n \n")

# This shows the mean errors for all methods
err_cols = (df['a_m_abs_err'], df['a_m_sq_err'], df['l_p_v_abs_err'], df['l_p_v_sq_err'])
name_list = df.columns.get_values()[4:]
errors = []
z = 0
for i in err_cols:
    err = round(i.mean(),2)
    name = name_list[z]
    z += 1
    errors.append((name + " : " + str(err)))
print("Errors: \n", errors)