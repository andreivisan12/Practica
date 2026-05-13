import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.style.use('seaborn-v0_8-whitegrid')

data_emisii = {
    'Țară': ['Luxemburg', 'Irlanda', 'Cehia', 'Media UE-27', 'Franța', 'România', 'Suedia'],
    'Emisii (t CO2e/loc)': [14.0, 11.4, 9.9, 7.2, 5.9, 5.5, 4.1]
}
df_emisii = pd.DataFrame(data_emisii).sort_values(by='Emisii (t CO2e/loc)', ascending=True)

plt.figure(figsize=(10, 6))
colors = ['#d62728' if x == 'România' else '#2ca02c' if x == 'Media UE-27' else '#1f77b4' for x in df_emisii['Țară']]
bars = plt.barh(df_emisii['Țară'], df_emisii['Emisii (t CO2e/loc)'], color=colors)
plt.axvline(x=7.2, color='green', linestyle='--', label='Media UE-27 (7.2 t/loc)')

plt.title('Emisii de GES per capita (Teritoriale, 2023)', fontsize=14)
plt.xlabel('Tone CO2 echivalent / locuitor', fontsize=12)

for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
             f'{bar.get_width()}', va='center', ha='left')
plt.legend()
plt.tight_layout()
plt.savefig('emisii_per_capita.png', dpi=300)
plt.close()

data_amprenta = {
    'Țară': ['România', 'Croația', 'Bulgaria', 'Spania', 'Italia', 'Germania', 'Suedia', 'Finlanda'],
    'Variație (%)': [10, 8, 1, -5, -7, -22, -39, -43]
}
df_amprenta = pd.DataFrame(data_amprenta).sort_values(by='Variație (%)', ascending=True)

plt.figure(figsize=(10, 6))
colors_amprenta = ['#d62728' if x > 0 else '#2ca02c' for x in df_amprenta['Variație (%)']]
bars_amprenta = plt.barh(df_amprenta['Țară'], df_amprenta['Variație (%)'], color=colors_amprenta)
plt.axvline(x=0, color='black', linewidth=1)

plt.title('Variația amprentei de consum de GES (2010 - 2023)', fontsize=14)
plt.xlabel('Variație procentuală (%)', fontsize=12)

for bar in bars_amprenta:
    val = bar.get_width()
    offset = 1 if val > 0 else -1
    plt.text(val + offset, bar.get_y() + bar.get_height()/2,
             f'{val}%', va='center', ha='center' if val > 0 else 'center')
plt.tight_layout()
plt.savefig('variatie_amprenta.png', dpi=300)
plt.close()

data_regiune = {
    'Regiune': ['România', 'Polonia', 'Bulgaria', 'Cehia', 'UE-27'],
    'Sărăcie energetică (%)': [28, 9, 24, 6, 9],
    'Regenerabile (%)': [25.8, 17, 23, 17, 24.5]
}
df_regiune = pd.DataFrame(data_regiune)

x = range(len(df_regiune['Regiune']))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar([i - width/2 for i in x], df_regiune['Sărăcie energetică (%)'], width, label='Populație în sărăcie energetică (%)', color='#d62728')
rects2 = ax.bar([i + width/2 for i in x], df_regiune['Regenerabile (%)'], width, label='Pondere regenerabile (%)', color='#2ca02c')

ax.set_ylabel('Procente (%)', fontsize=12)
ax.set_title('România în context regional: Sărăcie Energetică vs. Regenerabile (2023)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(df_regiune['Regiune'])
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.savefig('comparatie_regionala.png', dpi=300)
plt.close()