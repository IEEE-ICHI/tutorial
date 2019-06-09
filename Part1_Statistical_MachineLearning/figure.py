from matplotlib import pyplot as plt

def plot_roc_curve(fpr, tpr, auc, title, **kwargs):
    plt.figure(figsize=(10, 10), dpi=400, **kwargs)

    plt.plot(fpr, tpr, color='darkorange', label='ROC curve (area = %0.4f)' % auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=1, linestyle='--')

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.01])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

    plt.title('Receiver Operating Characteristic of %s' % title)
    plt.legend(loc="lower right")

    return plt.show()
