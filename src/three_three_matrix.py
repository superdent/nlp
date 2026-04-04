import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cm5 = np.array([
    [501292, 18289, 26129, 4357, 55507],
    [85340, 31780, 48937, 8386, 37843],
    [41072, 15400, 85365, 38708, 85023],
    [15117, 3583, 36514, 94839, 383874],
    [24249, 3484, 20925, 57450, 2907873]
])

cm3 = np.array([
    [cm5[0:2, 0:2].sum(), cm5[0:2, 2].sum(), cm5[0:2, 3:5].sum()],
    [cm5[2, 0:2].sum(),   cm5[2, 2],          cm5[2, 3:5].sum()],
    [cm5[3:5, 0:2].sum(), cm5[3:5, 2].sum(),  cm5[3:5, 3:5].sum()]
])

labels = ['Negativ (1-2)', 'Neutral (3)', 'Positiv (4-5)']

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(
    cm3,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=labels,
    yticklabels=labels,
    ax=ax
)
ax.set_xlabel('Predicted Label')
ax.set_ylabel('True Label')
ax.set_title('Confusion Matrix – Neurales Netz (errechnet)')
plt.tight_layout()
plt.savefig('confusion_matrix_3classes.png', dpi=150)
plt.show()