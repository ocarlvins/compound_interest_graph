import matplotlib.pyplot as plt
import numpy as np
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def f(item):
    try:
        return f'{item:,.2f}'
    except Exception as e:
        return str(item)
# li = list(zip(range(1, 14), range(14, 27)))

def linechart(*pairs, times=0):
    for num, pair in enumerate(pairs):
        axes = []
        axes.append([x[0] for x in pair])
        axes.append([x[1] for x in pair])
        # plt.plot(*[np.array(i) for i in axes], ls=":", label=f"{f(pair.initial)} @ {f(pair.perc)}% {'Compounded' if pair.compounding else ''}")
        plt.plot(*[np.array(i) for i in axes], ls="-",  label=f"{f(pair.initial)} @ {f(pair.perc)}% {'Compd' if pair.compounding else ''}")

    plt.legend()
    # plt.figure(figsize=(8, 6), dpi=300)
    plt.xticks(range(0, 21))
    if not times:
        plt.yticks(range(0, 32000000, 2500000))
    plt.ticklabel_format(useOffset=False)
    plt.ticklabel_format(style='plain', useLocale=True)
    plt.grid(color='green', linestyle='--', linewidth = 0.5)
    plt.xlabel("Time in years")
    plt.ylabel("Deposits")
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.title('Correct Plot')
    plt.tight_layout()
    plt.savefig('filename.svg', dpi=300)
    plt.show()
    """
    Introducing interactivity
    fig = plt.figure()

    with plt.ion():
        # interactive mode will be on
        # figures will automatically be shown
        fig2 = plt.figure()
        fig2.show()
    """