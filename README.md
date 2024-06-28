<!-- cSpell:disable -->

### RUN FILE

python ./scripts/<fileName.py>

Setting up a Python project for learning Matplotlib involves creating a structured environment where you can experiment with Matplotlib's plotting capabilities while maintaining good coding practices. Here’s a step-by-step guide to set up your Python project:

### 1. Project Setup

#### 1.1. Initialize Your Project

1. **Create a Project Directory**: Start by creating a new directory for your project:

   ```
   mkdir matplotlib-learning
   cd matplotlib-learning
   ```

2. **Initialize Virtual Environment**: It's a good practice to use a virtual environment to manage dependencies:
   ```
   python -m venv venv
   ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source venv/bin/activate
       ```

#### 1.2. Install Matplotlib and Dependencies

1. **Install Matplotlib**: Use pip to install Matplotlib and its dependencies:
   ```
   pip install matplotlib
   ```

### 2. Project Structure

Your project structure can be minimal for learning purposes:

```
/matplotlib-learning
├── /plots        <-- Directory for storing example plots
├── /scripts      <-- Python scripts for generating plots
│   └── example.py
└── README.md     <-- Project documentation
```

### 3. Writing Python Scripts

#### 3.1. Create Matplotlib Scripts

1. **Write Your First Script**: Create a Python script (`example.py` for instance) to generate a simple plot using Matplotlib:

   ```python
   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 10, 100)
   y = np.sin(x)

   plt.figure(figsize=(8, 6))
   plt.plot(x, y, label='sin(x)')
   plt.title('Simple Plot with Matplotlib')
   plt.xlabel('x')
   plt.ylabel('sin(x)')
   plt.legend()
   plt.grid(True)
   plt.savefig('plots/simple_plot.png')  # Save plot to file
   plt.show()
   ```

#### 3.2. Run Your Script

1. **Execute Your Script**: Run the Python script to generate and display a plot:
   ```
   python scripts/example.py
   ```
   - This will generate a plot (`simple_plot.png`) in the `plots` directory and display it using your default image viewer.

### 4. Enhancing Your Project

#### 4.1. Adding Documentation

1. **README.md**: Write a README file to document your project, including installation instructions, usage, and examples.

#### 4.2. Version Control

1. **Initialize Git Repository**: Initialize a Git repository in your project directory to track changes:
   ```
   git init
   ```
2. **Commit Your Changes**: Add and commit your code changes to Git:
   ```
   git add .
   git commit -m "Initial commit"
   ```

### 5. Additional Resources

- **Matplotlib Documentation**: Refer to the [Matplotlib documentation](https://matplotlib.org/stable/contents.html) for detailed guides and examples.
- **Python Virtual Environments**: Learn more about [Python virtual environments](https://docs.python.org/3/tutorial/venv.html) to manage project dependencies.

### Conclusion

Setting up a Python project for learning Matplotlib involves creating a structured environment with a virtual environment, installing Matplotlib, organizing scripts, and generating plots. This approach allows you to experiment with Matplotlib's plotting functionalities while maintaining good coding practices and documentation habits.
