from flask import Flask, render_template, request, Response

import matplotlib.pyplot as plt
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contour')
def contour_chart():
    # Generate sample data or use data from request.args
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    # Create the contour plot
    fig, ax = plt.subplots()
    contour = ax.contourf(X, Y, Z, cmap='viridis')
    ax.set_title('Contour Plot')
    fig.colorbar(contour)

    # Save plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Return image as a response
    return Response(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)