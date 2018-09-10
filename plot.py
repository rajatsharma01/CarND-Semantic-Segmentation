import matplotlib.pyplot as plt

with open('mean_loss.csv', 'r') as loss_file:
    losses = [float(loss_str) for loss_str in loss_file.read().split()]
    x = [i+1 for i in range(len(losses))]
    plt.figure(figsize=(12,3))
    plt.scatter(x, losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Mean Loss Per Epoch')
    plt.grid()
    plt.savefig('loss_plot.png')
