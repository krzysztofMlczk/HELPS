import matplotlib.pyplot as plt
import numpy as np

from src.report.common.colors import colors, edges
from src.report.overall_score.overall_score_calculator import get_overall_scores

overall_scores = get_overall_scores()

data = {
    "GPT-4": overall_scores["gpt-4"],
    "Gemini 1.5 Pro": overall_scores["gemini-1-5-pro"],
    "Claude 3.5 Sonnet": overall_scores["claude-3-5-sonnet"],
}
colors = [colors["gpt-4"], colors["gemini-1-5-pro"], colors["claude-3-5-sonnet"]]
edge_colors = [edges["gpt-4"], edges["gemini-1-5-pro"], edges["claude-3-5-sonnet"]]

# Extract keys and values from the dictionary
categories = list(data.keys())
values = list(data.values())

# Create the bar chart
plt.figure(figsize=(8, 5))  # Set the figure size
# Draw background grid
# Set y-axis ticks at intervals of 0.1
plt.yticks(np.arange(0, 1, 0.1))
# Add a grid with major lines at each tick
plt.grid(axis='y', linestyle='--', alpha=0.3, zorder=0)
# Draw bars
bars = plt.bar(
    categories,
    values,
    color=colors,
    edgecolor=edge_colors,
    width=0.5,
    zorder=3
)

# Display the exact values on top of the bars
for i, bar in enumerate(bars):
    color = edge_colors[i]
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval - 0.05,  # Position the text above the bar
             f"{yval:.2f}", ha='center', va='bottom', fontsize=10, color=color)

# Add labels and title
# plt.xlabel("Categories")
# plt.ylabel("Values")
plt.title("HELPS benchmark")


pdf_file = "overall_score_chart.pdf"
plt.savefig(pdf_file, format="pdf", bbox_inches="tight")

# Close the figure
plt.close()
