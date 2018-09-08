import matplotlib.pyplot as plt

with open('mean_loss.csv', 'r') as loss_file:
    losses = [float(loss_str) for loss_str in loss_file.read().split()]
    epochs = [e for e in range(2, 101)]
    print(len(epochs))
    plt.figure(figsize=(12,3))
    plt.scatter(epochs, losses[1:])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.xlim(0,102)
    plt.ylim(0)
    plt.title('Training Mean Loss for Epochs 2-100')
    plt.grid()
    plt.savefig('loss_plot.png')
