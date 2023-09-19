from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

from utils import generate_dataframe

the_data_frame = generate_dataframe()
the_data_frame = the_data_frame.dropna()

# Set a seed
seed = 42

def regression_model(the_data_frame):
    X_reg = the_data_frame[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']]
    y_reg = the_data_frame['body_mass_g']

    X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=seed)

    regression_model = LinearRegression()
    regression_model.fit(X_reg_train, y_reg_train)

    y_reg_pred = regression_model.predict(X_reg_test)

    regression_mse = mean_squared_error(y_reg_test, y_reg_pred)
    print(f"Regression Mean Squared Error: {regression_mse:.2f}")


def classification_model(the_data_frame):
    the_data_frame['species'] = the_data_frame['species'].astype('category')
    the_data_frame['species_encoded'] = the_data_frame['species'].cat.codes

    X_cls = the_data_frame[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
    y_cls = the_data_frame['species_encoded']

    X_cls_train, X_cls_test, y_cls_train, y_cls_test = train_test_split(X_cls, y_cls, test_size=0.2, random_state=seed)

    classification_model = RandomForestClassifier(random_state=seed)
    classification_model.fit(X_cls_train, y_cls_train)

    y_cls_pred = classification_model.predict(X_cls_test)

    classification_accuracy = accuracy_score(y_cls_test, y_cls_pred)
    print(f"Classification Accuracy: {classification_accuracy:.2f}")


#run the models
regression_model(the_data_frame)
classification_model(the_data_frame)
