"""
Plotting module.
Contains function to plot actual vs predicted stock prices in a Tkinter canvas.
"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_trend(dates, real_prices, predicted_prices, ticker, canvas_frame):
    """
    Plot actual and predicted closing prices on a matplotlib figure embedded in Tkinter.
    """
    plt.close('all')
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dates, real_prices, label="Actual Closing Prices", color='blue')
    ax.plot(dates, predicted_prices, label="Predicted Closing Prices", color='red', linestyle='dashed')
    ax.set_xlabel("Date")
    ax.set_ylabel("Stock Price")
    ax.set_title(f"Stock Price Trend for {ticker}")
    ax.legend()
    for widget in canvas_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
