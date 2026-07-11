import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
from typing import Tuple, Optional, Dict, List
import warnings

class LogisticRegressionApp:
    """
    A Streamlit application for visualizing Logistic Regression classification.
    """
    
    # Solver-penalty compatibility dictionary
    SOLVER_PENALTY_MAP = {
        'newton-cg': ['l2', 'none'],
        'lbfgs': ['l2', 'none'],
        'liblinear': ['l1', 'l2'],
        'sag': ['l2', 'none'],
        'saga': ['l1', 'l2', 'elasticnet', 'none']
    }
    
    def __init__(self):
        self.setup_page_config()
        self.X: Optional[np.ndarray] = None
        self.y: Optional[np.ndarray] = None
        self.clf: Optional[LogisticRegression] = None
        
    def setup_page_config(self):
        """Configure the Streamlit page settings."""
        st.set_page_config(
            page_title="Logistic Regression Visualizer",
            page_icon="📊",
            layout="wide"
        )
        plt.style.use('fivethirtyeight')
    
    def get_valid_penalties(self, solver: str) -> List[str]:
        """Get valid penalties for a given solver."""
        return self.SOLVER_PENALTY_MAP.get(solver, [])
        
    def create_sidebar(self) -> dict:
        """
        Create the sidebar with all input parameters.
        
        Returns:
            dict: Dictionary containing all user-selected parameters
        """
        st.sidebar.markdown("# Logistic Regression Classifier")
        
        # First get solver as it affects penalty options
        solver = st.sidebar.selectbox(
            'Solver',
            ('lbfgs', 'newton-cg', 'liblinear', 'sag', 'saga'),
            help="Algorithm to use in the optimization problem"
        )
        
        # Get valid penalties for selected solver
        valid_penalties = self.get_valid_penalties(solver)
        
        # Show penalty selection with only valid options
        penalty = st.sidebar.selectbox(
            'Regularization',
            valid_penalties,
            help=f"Valid penalties for {solver} solver"
        )
        
        params = {
            'dataset': st.sidebar.selectbox(
                'Select Dataset',
                ('Binary', 'Multiclass')
            ),
            'penalty': penalty,
            'c_input': st.sidebar.number_input(
                'C (Inverse of regularization strength)',
                min_value=0.1,
                max_value=10.0,
                value=1.0,
                step=0.1,
                help="Smaller values indicate stronger regularization"
            ),
            'solver': solver,
            'max_iter': st.sidebar.slider(
                'Max Iterations',
                min_value=100,
                max_value=1000,
                value=100,
                step=50
            ),
            'multi_class': st.sidebar.selectbox(
                'Multi Class Strategy',
                ('auto', 'ovr', 'multinomial')
            )
        }
        
        # Only show l1_ratio if elasticnet is selected
        if penalty == 'elasticnet':
            params['l1_ratio'] = st.sidebar.slider(
                'l1 Ratio',
                min_value=0,
                max_value=100,
                value=50,
                help="Mix ratio between l1 and l2 regularization for elasticnet penalty"
            ) / 100
        else:
            params['l1_ratio'] = None
            
        return params
    
    def load_data(self, dataset: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Load the selected dataset.
        
        Args:
            dataset (str): Type of dataset to generate
            
        Returns:
            Tuple containing features (X) and labels (y)
        """
        if dataset == "Binary":
            X, y = make_blobs(n_samples=300, n_features=2, centers=2, random_state=6)
        else:
            X, y = make_blobs(n_samples=300, n_features=2, centers=3, random_state=2)
        return X, y
    
    def create_model(self, params: dict) -> LogisticRegression:
        """
        Create and return a LogisticRegression model with the specified parameters.
        
        Args:
            params (dict): Model parameters
            
        Returns:
            LogisticRegression: Configured model instance
        """
        return LogisticRegression(
            penalty=params['penalty'],
            C=params['c_input'],
            solver=params['solver'],
            max_iter=params['max_iter'],
            multi_class=params['multi_class'],
            l1_ratio=params['l1_ratio']
        )
    
    def draw_meshgrid(self, X: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Create a meshgrid for plotting decision boundaries.
        
        Args:
            X (np.ndarray): Input features
            
        Returns:
            Tuple containing meshgrid components and input array
        """
        margin = 0.5
        x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
        y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
        
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, 0.02),
            np.arange(y_min, y_max, 0.02)
        )
        
        return xx, yy, np.c_[xx.ravel(), yy.ravel()]
    
    def plot_results(self, X: np.ndarray, y: np.ndarray, clf: LogisticRegression):
        """
        Create and display the visualization plots.
        
        Args:
            X (np.ndarray): Input features
            y (np.ndarray): True labels
            clf (LogisticRegression): Trained classifier
        """
        col1, col2 = st.columns(2)
        
        with col1:
            # Decision Boundary Plot
            fig, ax = plt.subplots(figsize=(10, 6))
            xx, yy, input_array = self.draw_meshgrid(X)
            
            # Plot decision boundary
            Z = clf.predict(input_array)
            Z = Z.reshape(xx.shape)
            ax.contourf(xx, yy, Z, alpha=0.4, cmap='rainbow')
            
            # Plot data points
            scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='rainbow', edgecolor='black')
            plt.colorbar(scatter)
            
            plt.xlabel("Feature 1")
            plt.ylabel("Feature 2")
            plt.title("Decision Boundary")
            st.pyplot(fig)
        
        with col2:
            # Confusion Matrix
            y_pred = clf.predict(X)
            cm = confusion_matrix(y, y_pred)
            
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title("Confusion Matrix")
            plt.xlabel("Predicted")
            plt.ylabel("True")
            st.pyplot(fig)
        
        # Classification Report
        st.subheader("Classification Report")
        report = classification_report(y, y_pred)
        st.text(report)
        
        # Model Parameters
        st.subheader("Model Parameters")
        model_info = {
            'Coefficients Shape': clf.coef_.shape,
            'Number of Iterations': clf.n_iter_[0] if isinstance(clf.n_iter_, tuple) else clf.n_iter_,
            'Classes': clf.classes_.tolist()
        }
        # Convert all values to lists or simple types for JSON serialization
        model_info_serializable = {
            'Coefficients Shape': list(model_info['Coefficients Shape']),
            'Number of Iterations': int(model_info['Number of Iterations']),
            'Classes': model_info['Classes']
        }
        st.json(model_info_serializable)
    
    def run(self):
        """Run the Streamlit application."""
        params = self.create_sidebar()
        
        try:
            # Load and split data
            X, y = self.load_data(params['dataset'])
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Initial plot
            fig, ax = plt.subplots(figsize=(10, 6))
            scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='rainbow', edgecolor='black')
            plt.colorbar(scatter)
            plt.xlabel("Feature 1")
            plt.ylabel("Feature 2")
            plt.title("Initial Data Distribution")
            st.pyplot(fig)
            
            if st.sidebar.button('Train Model'):
                with st.spinner('Training model...'):
                    # Create and train model
                    clf = self.create_model(params)
                    
                    with warnings.catch_warnings():
                        warnings.filterwarnings('ignore')
                        clf.fit(X_train, y_train)
                    
                    # Display results
                    self.plot_results(X_test, y_test, clf)
                    
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please try different parameters or refresh the page.")

if __name__ == "__main__":
    app = LogisticRegressionApp()
    app.run()