# Project : Password Strength Classification using Support Vector Machine (SVM)
### Project Type : Minor Project
### Name : Navneeth Rajeev Menon
### Admission Number : AA.SC.U3BCA2307091

## Abstract :

This project develops a machine learning system to classify passwords into
three strength categories — **Weak, Medium, and Strong** — using static features
extracted from password strings. A synthetic dataset is generated (or a real-
world dataset can be used), features such as length, counts of uppercase/
lowercase/digits/symbols, estimated entropy, repetitive characters, and
sequential substrings are extracted, and an SVM classifier is trained using
Scikit-learn. The system aims to provide an interpretable, lightweight model for
password strength analysis that can aid password-strength meters and
password policy enforcement systems.

## Assumptions/Declarations :

1. This is a classification (supervised) task using static features only (no runtime
analysis or external lookups).
2. The model is not meant to replace centralized password policies but to illustrate
automatic classification and detection of weak passwords for educational
purposes.

## Main Objective/Deliverable :

Build a reproducible Python pipeline to generate a password dataset, extract
interpretable features, train an SVM classifier, and evaluate its performance
(accuracy, precision, recall, confusion matrix).
