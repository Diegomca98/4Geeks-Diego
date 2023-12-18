import os

parent = 'C:/Users/diego/Documents/courses/4geeks/4Geeks-Diego/'

directories = [
    'Random-Variables', 'Hypothesis-Testing', 'Algorithm-Optimization', 'ML-Ops', 'Intro-to-SQL', 'Web-Scraping', 'API-Requests', 'Exploratory-Data-Analysis','Your-First-ML-Algorithm', 'Linear-Regression', 'Regularized-Linear-Regression', 'Decision-Tree-Algorithm', 'Random-Forest-Algorithm', 'Boosting-Algorithms', 'Naive-Bayes-Algorithm', 'K-Nearest-Neighbors', 'Unsupervised-Learning', 'Time-Series-Forecasting', 'Intro-to-Deep-Learning', 'Intro-to-NLP', 'ML-Webapp-Using-Flask', 'ML-Webapp-Using-Streamlit', 'Cloud-Computing-for-ML', 'Final-Project', 'Additional-Resources'
]

num = 6
for i in directories:
    if num > 9:
        path = f'M{num}-{i.replace(" ", "-")}'
        full_path = os.path.join(parent, path)
        os.mkdir(full_path)
        num += 1
    if num < 10:
        path = f'M0{num}-{i.replace(" ", "-")}'
        full_path = os.path.join(parent, path)
        os.mkdir(full_path)
        num+=1