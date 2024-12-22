import matplotlib.pyplot as plt
import numpy as np

from src.report.common.colors import colors, edges
from src.report.per_metric.metric_score_calculator import calculate_for_metric

# Data
categories = ["helpfulness", "relevancy", "brevity"]
models = ["GPT-4", "Gemini 1.5 Pro", "Claude 3.5 Sonnet"]
scores = [
    [  # Scores for GPT-4
        calculate_for_metric("gpt-4", "helpfulness"),
        calculate_for_metric("gpt-4", "relevancy"),
        calculate_for_metric("gpt-4", "brevity"),
    ],
    [  # Scores for Gemini 1.5
        calculate_for_metric("gemini-1-5-pro", "helpfulness"),
        calculate_for_metric("gemini-1-5-pro", "relevancy"),
        calculate_for_metric("gemini-1-5-pro", "brevity"),
    ],
    [  # Scores for Claude-3.5 Sonnet
        calculate_for_metric("claude-3-5-sonnet", "helpfulness"),
        calculate_for_metric("claude-3-5-sonnet", "relevancy"),
        calculate_for_metric("claude-3-5-sonnet", "brevity"),
    ],
]

# Parameters
x = np.arange(len(categories))  # X positions for the categories
width = 0.2  # Width of the bars

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
# Draw background grid
# Set y-axis ticks at intervals of 0.1
plt.yticks(np.arange(0, 1, 0.1))
# Add a grid with major lines at each tick
plt.grid(axis="y", linestyle="--", alpha=0.3, zorder=0)
# Draw bars
bars_gpt = ax.bar(
    x - width,
    scores[0],
    width,
    label=models[0],
    color=colors["gpt-4"],
    edgecolor=edges["gpt-4"],
    zorder=3,
)
bars_gemini = ax.bar(
    x,
    scores[1],
    width,
    label=models[1],
    color=colors["gemini-1-5-pro"],
    edgecolor=edges["gemini-1-5-pro"],
    zorder=3,
)
bars_claude = ax.bar(
    x + width,
    scores[2],
    width,
    label=models[2],
    color=colors["claude-3-5-sonnet"],
    edgecolor=edges["claude-3-5-sonnet"],
    zorder=3,
)

# Display the exact values on top of the bars
for i, bar in enumerate(bars_gpt):
    color = edges["gpt-4"]
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval - 0.05,  # Position the text above the bar
             f"{yval:.2f}", ha='center', va='bottom', fontsize=10, color=color)

for i, bar in enumerate(bars_gemini):
    color = edges["gemini-1-5-pro"]
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval - 0.05,  # Position the text above the bar
             f"{yval:.2f}", ha='center', va='bottom', fontsize=10, color=color)

for i, bar in enumerate(bars_claude):
    color = edges["claude-3-5-sonnet"]
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval - 0.05,  # Position the text above the bar
             f"{yval:.2f}", ha='center', va='bottom', fontsize=10, color=color)

# Customization
# ax.set_xlabel("Categories")
# ax.set_ylabel("Avg Score")
ax.set_title("Avg score per metric, per model")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylim(0, 1)  # Adjust y-axis range
ax.legend()

# Styling similar to the uploaded image
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.set_ticks_position("left")
ax.xaxis.set_ticks_position("bottom")
ax.tick_params(axis="both", which="both", length=0)
plt.xticks(fontsize=12, rotation=0)
plt.yticks(fontsize=12)

# Save plot to a file
output_file = "avg_per_metric_per_model.pdf"
plt.tight_layout()
plt.savefig(output_file, dpi=300)  # Adjust DPI for quality
print(f"Chart saved as {output_file}")

# Optional: Display the chart
# plt.show()
