**Objective**

The goal of this project is to cluster customers based on their anual income and spending score which can include:

Purchase history

Demographics (age, income, etc.)

Using these clusters, businesses can:
Personalize marketing campaigns
Identify high-value customers
Improve product recommendations

**Workflow**

The general workflow for the project is as follows:

Data Collection: Collect customer data from internal databases or external sources.

Data Preprocessing: Clean and prepare the data (handling missing values, scaling, etc.).

Exploratory Data Analysis (EDA): Visualize and understand the key patterns in the data.

Clustering: Apply clustering algorithm **K-Means** to group similar customers.

Evaluation: Use evaluation metrics like the silhouette score and elbow method to assess the quality of the clusters.

Reporting: Summarize findings and visualizations into a report that highlights insights and actionable recommendations.

**Technologies Used**

Programming Language: Python 3.9

Libraries:

pandas, numpy for data manipulation

scikit-learn for machine learning algorithms

matplotlib, seaborn for data visualization

flask for utilizing the trined model for future prediction.

**Installation and Setup**

Clone this repository:  git clone https://github.com/PKD-DB/vcc_assignment_project.git

Create a virtual environment and activate it : python -m venv myvenv

Install the required dependencies:  pip install -r requirements.txt

To run the project, execute the following command: python run main.py

**Deployment:**

This model deployed on app engine on GCP

End point to access the app running on GCP.

https://vcc-assignment-g23ai2014.as.r.appspot.com/
