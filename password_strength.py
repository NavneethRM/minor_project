import random
import string
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#TODO: Gen Password

def generate_password(length, charset):
    return ''.join(random.choice(charset) for _ in range(length))

passwords = []
labels = []

# Weak passwords
for _ in range(200):
    pwd = generate_password(random.randint(4, 6), string.ascii_lowercase)
    passwords.append(pwd)
    labels.append(0)  # Weak

# Medium passwords
for _ in range(200):
    charset = string.ascii_lowercase + string.digits
    pwd = generate_password(random.randint(7, 9), charset)
    passwords.append(pwd)
    labels.append(1)  # Medium

# Strong passwords
for _ in range(200):
    charset = string.ascii_letters + string.digits + string.punctuation
    pwd = generate_password(random.randint(10, 14), charset)
    passwords.append(pwd)
    labels.append(2)  # Strong


def extract_features(password):
    length = len(password)
    upper = sum(1 for c in password if c.isupper())
    lower = sum(1 for c in password if c.islower())
    digits = sum(1 for c in password if c.isdigit())
    symbols = sum(1 for c in password if c in string.punctuation)
    return [length, upper, lower, digits, symbols]

X = np.array([extract_features(p) for p in passwords])
y = np.array(labels)

#TODO: Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

#TODO: Model training

model = SVC(kernel="rbf", C=1.0, gamma="scale")
model.fit(X_train, y_train)

#TODO: Evaluation

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test, y_pred,
    target_names=["Weak", "Medium", "Strong"]
))
