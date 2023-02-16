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


def chart(*pairs, times=0, show_processor=lambda x: x.show()):
    for num, pair in enumerate(pairs):
        axes = []
        axes.append([x[0] for x in pair])
        axes.append([x[1] for x in pair])
        # plt.plot(*[np.array(i) for i in axes], ls=":", label=f"{f(pair.initial)} @ {f(pair.perc)}% {'Compounded' if pair.compounding else ''}")
        plt.plot(*[np.array(i) for i in axes], ls="-",  label=f"{f(pair.initial)} @ {f(pair.perc)}% {'Compd' if pair.compounding else ''}")

    plt.legend()
    # plt.figure(figsize=(8, 6), dpi=300)
    plt.xticks(range(0, 21))
    # plt.ticklabel_format(useOffset=False)
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)
    plt.ticklabel_format(style='plain', useLocale=True)
    plt.grid(color='green', linestyle='--', linewidth = 0.5)
    return plt

    """
    Introducing interactivity
    fig = plt.figure()

    with plt.ion():
        # interactive mode will be on
        # figures will automatically be shown
        fig2 = plt.figure()
        fig2.show()
    """


def deposit_chart(*args, **kwargs):
    plot = chart(*args, **kwargs)
    if not kwargs['times']:
        plot.yticks(range(0, 32000000, 2500000))
    plot.xlabel("Time in years")
    plot.ylabel("Deposits")
    plot.title('Deposits Accumulated')
    plot.savefig('deposits.svg', dpi=300)
    plt.tight_layout()
    plot.show()


def monthly_return_chart(*args, **kwargs):
    plot = chart(*args, **kwargs)
    if not kwargs['times']:
        plot.yticks(range(0, 450000, 25000))
    plot.xlabel("Time in years")
    plot.ylabel("Monthly Return")
    plot.title('Monthly Return Chart')
    plot.savefig('monthly_return.svg', dpi=300)
    plt.tight_layout()
    plot.show()


