import pandas as pd

df = pd.read_csv("task/stackoverflow_qa.csv")

q1 = df[pd.to_datetime(df["creationdate"]) < "2014-01-01"]

q2 = df[df["score"] > 50]

q3 = df[(df["score"] >= 50) & (df["score"] <= 100)]

q4 = df[df["ans_name"] == "Scott Boston"]

users = ["Unutbu", "Mike Pennington", "Scott Boston", "Demitri", "doug"]
q5 = df[df["ans_name"].isin(users)]

q6 = df[
    (pd.to_datetime(df["creationdate"]) >= "2014-03-01") &
    (pd.to_datetime(df["creationdate"]) <= "2014-10-31") &
    (df["ans_name"] == "Unutbu") &
    (df["score"] < 5)
]

q7 = df[((df["score"] >= 5) & (df["score"] <= 10)) | (df["viewcount"] > 10000)]

# 8. Questions NOT answered by Scott Boston
q8 = df[df["ans_name"] != "Scott Boston"]






import pandas as pd

titanic_df = pd.read_csv("task/titanic.csv")

h3_q1 = titanic_df[(titanic_df["Sex"] == "female") & 
                   (titanic_df["Pclass"] == 1) & 
                   (titanic_df["Age"].between(20, 30))]

h3_q2 = titanic_df[titanic_df["Fare"] > 100]

h3_q3 = titanic_df[(titanic_df["Survived"] == 1) & 
                   (titanic_df["SibSp"] == 0) & 
                   (titanic_df["Parch"] == 0)]

h3_q4 = titanic_df[(titanic_df["Embarked"] == "C") & (titanic_df["Fare"] > 50)]

h3_q5 = titanic_df[(titanic_df["SibSp"] > 0) & (titanic_df["Parch"] > 0)]

h3_q6 = titanic_df[(titanic_df["Age"] <= 15) & (titanic_df["Survived"] == 0)]

h3_q7 = titanic_df[titanic_df["Cabin"].notna() & (titanic_df["Fare"] > 200)]

h3_q8 = titanic_df[titanic_df["PassengerId"] % 2 == 1]

h3_q9 = titanic_df[titanic_df["Ticket"].map(titanic_df["Ticket"].value_counts()) == 1]

h3_q10 = titanic_df[(titanic_df["Sex"] == "female") &
                    (titanic_df["Pclass"] == 1) &
                    (titanic_df["Name"].str.contains("Miss"))]
