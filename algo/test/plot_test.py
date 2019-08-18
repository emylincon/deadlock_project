import matplotlib.pyplot as plt

deadlock = [1]


def plot_deadlock():
    cols = ['r']
    text = str(deadlock[-1] - 1) + " Deadlock resolved"
    wedges, texts, autotexts = plt.pie(deadlock, shadow=True, autopct=text,
                                       textprops=dict(rotation_mode='anchor', color="w", ha='left'), colors=cols)

    plt.setp(autotexts, size=9, weight="bold")

    #ax5.set_title("Deadlock Resolved Counter")
    plt.show()

plot_deadlock()