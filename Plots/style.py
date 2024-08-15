from matplotlib import pyplot as plt

plt.rcParams.update({
    'font.size': 15,
    'axes.titlesize': 15,
    'axes.labelsize': 15,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 15
})

def get_figsize(name: str) -> tuple:
    return fig_dict.get(name)
    
half_fig = (3, 3)
figsize = (7.5, 5)
long_fig = (4, 13)

fig_dict = {
    'fig': figsize,
    'half_fig': half_fig,
    'long_fig': long_fig,
}