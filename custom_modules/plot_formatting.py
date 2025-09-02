import matplotlib.pyplot as plt

def percentage_stacked_bars(plot, threshold=0):
    """Add percentage numbers to stacked bar plot."""
    for p in plot.patches:
        width = p.get_width()
        height = p.get_height()
        x = p.get_x() + width / 2
        y = p.get_y() + height / 2

        if height > threshold:
            plot.text(x, y, f'{height:.0f}%', ha="center", va="center", fontsize=7)
 

def ci_bar(counts_df, group="group"):
    """Plot confidence intervals on bar plot."""
    plt.errorbar(
        x=counts_df[group],
        y=counts_df["proportion"],
        yerr=[
            counts_df["proportion"] - counts_df["ci_lower"],
            counts_df["ci_upper"] - counts_df["proportion"],
        ],
        fmt="none",
        capsize=5,
        color="black",
    )


def estimates_bar(counts_df, bar_plot):
    """Add proportion estimates and confidence intervals to bar plot."""
    for index, row in counts_df.iterrows():
        bar_plot.text(
            index + 0.1,
            row["proportion"],
            f"{row['proportion']:.1%}",
            color="black",
            ha="left",
            va="bottom",
            fontweight="bold",
            fontsize=11,
        )
        ci_text = f"{row['ci_lower']:.1%} - {row['ci_upper']:.1%}"
        bar_plot.text(
            index,
            row["proportion"] - 0.035,
            ci_text,
            color="black",
            ha="center",
            va="top",
            fontstyle="oblique",
        )


def horizontal_bars_estimates_ci(df, col):
    """Add proportion estimates and confidence intervals to horizontal bar plot."""
    for i in range(len(df)):
        ci_lower = df["ci_lower"].iloc[i]
        ci_upper = df["ci_upper"].iloc[i]
        plt.errorbar(
            df[col].iloc[i],
            i + 0.2,
            xerr=[
                [df[col].iloc[i] - ci_lower],
                [ci_upper - df[col].iloc[i]],
            ],
            fmt=".",
            color="black",
            label="Analytical CI" if i == 0 else "",
            capsize=5,
        )
        plt.text(
            ci_lower - 0.005,
            i + 0.2,
            f"{ci_lower:.2%}",
            va="center",
            ha="right",
            fontsize=8,
            color="black",
        )
        plt.text(
            ci_upper + 0.005,
            i + 0.2,
            f"{ci_upper:.2%}",
            va="center",
            ha="left",
            fontsize=8,
            color="black",
        )

    for i, rate in enumerate(df[col]):
        plt.text(
            rate + 0.001, i, f"{rate:.2%}", va="center", fontsize=10, fontweight="bold"
        )


def horizontal_bars_estimates_2cis(df, col):  
    """Add proportion estimates and two confidence intervals (analytical and bootstrapped) to horizontal bar plot."""      
    for i in range(len(df)):
        ci_lower = df["ci_lower"].iloc[i]
        ci_upper = df["ci_upper"].iloc[i]
        plt.errorbar(
            df[col].iloc[i],
            i + 0.2,
            xerr=[
                [df[col].iloc[i] - ci_lower],
                [ci_upper - df[col].iloc[i]],
            ],
            fmt=".",
            color="black",
            label="Analytical CI" if i == 0 else "",
            capsize=5,
        )
        plt.text(
            ci_lower - 0.005,
            i + 0.2,
            f"{ci_lower:.2%}",
            va="center",
            ha="right",
            fontsize=8,
            color="black",
        )
        plt.text(
            ci_upper + 0.005,
            i + 0.2,
            f"{ci_upper:.2%}",
            va="center",
            ha="left",
            fontsize=8,
            color="black",
        )

    for i in range(len(df)):
        boot_ci_lower = df["boot_ci_lower"].iloc[i]
        boot_ci_upper = df["boot_ci_upper"].iloc[i]
        plt.errorbar(
            df[col].iloc[i],
            i - 0.2,
            xerr=[
                [df[col].iloc[i] - boot_ci_lower],
                [boot_ci_upper - df[col].iloc[i]],
            ],
            fmt=".",
            color="blue",
            label="Bootstrapped CI" if i == 0 else "",
            capsize=5,
        )
        plt.text(
            boot_ci_lower - 0.005,
            i - 0.2,
            f"{boot_ci_lower:.2%}",
            va="center",
            ha="right",
            fontsize=8,
            color="blue",
        )
        plt.text(
            boot_ci_upper + 0.005,
            i - 0.2,
            f"{boot_ci_upper:.2%}",
            va="center",
            ha="left",
            fontsize=8,
            color="blue",
        )

    for i, rate in enumerate(df[col]):
        plt.text(
            rate + 0.001, i, f"{rate:.2%}", va="center", fontsize=10, fontweight="bold"
        )