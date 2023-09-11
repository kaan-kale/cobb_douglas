import matplotlib.pyplot as plt
import numpy as np

# Create a function that outputs, X, Y meshgrid and Z array for cobb_douglas utility function
def cobb_douglas(alpha, beta, num_points=100):
    """
    Create a function that outputs, X, Y meshgrid and Z array for cobb_douglas utility function
    Inputs: alpha and beta
    Output: X, Y meshgrid and Z array
    """
    # Create the grid
    x = np.linspace(0, 10, num_points)
    y = np.linspace(0, 10, num_points)
    X, Y = np.meshgrid(x, y)

    # Create the function
    Z = X**alpha * Y**beta

    return X, Y, Z

def plot_cobb_douglas(alpha, beta, file_name, **kwargs):
    """
    Plot Cobb-Douglas production function and save it to a file, and there should be countour planes on the vertical axis.
    Inputs: alpha, beta, and the file name
    Output: None
    """
    # Set the colormap
    cmap = plt.colormaps['viridis']

    # Create a 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(10, 0)
    ax.set_ylim(10, 0)

    num_points = kwargs.get('num_points')
    X, Y, Z = cobb_douglas(alpha, beta, num_points)

    # Plot the surface
    ax.plot_surface(X, Y, Z, cmap=cmap, edgecolor='none')

    # Add a contour plane 
    y_contour = kwargs.get('y_contour')
    if y_contour:
        contour_levels = [y_contour, 10]
        Z[-1] = np.full(100, Z.max())
        cset = ax.contourf(X, Y, Z, zdir='y', offset=y_contour, colors='#e73e3e', levels=contour_levels, alpha=0.75)

    # Adjust the viewing angle 
    ax.view_init(12, 70)

    # Set the labels
    labels = kwargs.get('labels')
    x_label = labels.get('x')
    y_label = labels.get('y')
    z_label = labels.get('z')
    ax.set_xlabel(x_label, labelpad=-10)
    ax.set_ylabel(y_label, labelpad=-10)
    ax.set_zlabel(z_label, labelpad=-10)

    # Close x, y and z ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Make the figure bigger and closer to the viewer
    fig.set_size_inches(10, 8)
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

    # Save the figure
    plt.savefig(file_name)

def plot_cobb_douglas_contour(alpha, beta, file_name, **kwargs):
    num_points = kwargs.get('num_points')
    X, Y, Z = cobb_douglas(alpha, beta, num_points) 

    # Create a 3D figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set the limits
    ax.set_xlim(10, 0)
    ax.set_ylim(10, 0)
    
    # Define levels for contour lines
    zdir = kwargs.get('zdir')
    num_levels = kwargs.get('num_levels')

    if zdir == 'z':
        levels = np.linspace(Z.min(), Z.max(), num_levels)
    else:
        levels = np.linspace(Y.min(), Y.max(), num_levels)

    # Create the contour plot
    ax.contour(X, Y, Z, zdir=zdir, cmap='viridis', levels=levels)  

    # Adjust the viewing angle
    degrees = kwargs.get('degrees') 
    if degrees:
        ax.view_init(*degrees)

    # Close x, y and z ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Set the labels
    labels = kwargs.get('labels')
    x_label = labels.get('x')
    y_label = labels.get('y')
    z_label = labels.get('z')
    ax.set_xlabel(x_label, labelpad=-10)
    ax.set_ylabel(y_label, labelpad=-10)
    ax.set_zlabel(z_label, labelpad=-10)

    # Make the figure bigger and closer to the viewer
    fig.set_size_inches(10, 8)
    fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

    # Save the figure
    plt.savefig(file_name)

if __name__ == "__main__":
    kwargs = {
        'degrees': (12, 70),
        'labels': {
            'x': 'X',
            'y': 'Y',
            'z': 'Utility'
        },
        'num_points': 100,
    }
    # plot_cobb_douglas(0.3, 0.5, 'cobb_douglas.png')  
     
    kwargs = {
        'degrees': (30, 60),
        'labels': {
            'x': 'X',
            'y': 'Y',
            'z': 'Utility'
        },
        'num_points': 100,
        'num_levels': 25,
        'zdir': 'x'
        }   
    
    plot_cobb_douglas_contour(0.3, 0.4, 'cobb_douglas_contour.png', **kwargs)