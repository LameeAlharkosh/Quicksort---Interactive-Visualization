# utils.py
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_palette("pastel")

def plot_array_state(array):
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(range(len(array)), array)

    # Add the numerical label inside each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,  # x‐position: center of the bar
            height / 2,                         # y‐position: halfway up the bar
            str(int(height)),                   # label text
            ha='center',                        # horizontal alignment
            va='center',                        # vertical alignment
            color='black',                      # text color
            fontsize=12
        )

    ax.set_xticks(range(len(array)))
    ax.set_xticklabels([str(i) for i in range(len(array))])
    ax.set_ylim(0, max(array) + 1)
    ax.set_title("Array State", fontsize=14, weight="bold")
    st.pyplot(fig)

