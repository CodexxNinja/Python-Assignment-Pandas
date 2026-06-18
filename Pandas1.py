import pandas as pd
import numpy as np

student_data = {
    "Name": ["Rahul", "Priya", "Amit", "Neha"],
    "Age": [22, 21, 23, 22],
    "City": ["Pune", "Mumbai", "Nashik", "Delhi"]
}

product_data = {
    "Product": ["Laptop", "Mobile", "Shoes", "TV", "Watch"],
    "Category": ["Electronics", "Electronics", "Fashion", "Electronics", "Fashion"],
    "Price": [55000, 20000, 3000, 40000, 5000],
    "Quantity": [5, 10, 8, 3, 12]
}

df = pd.DataFrame(student_data)
products = pd.DataFrame(product_data)

df.to_csv("students.csv", index=False)
df.to_excel("students.xlsx", index=False)
products.to_csv("products.csv", index=False)

def f1():
    print(pd.Series([10, 20, 30, 40]))

def f2():
    print(pd.Series([100, 200, 300], index=['a', 'b', 'c']))

def f3():
    print(pd.Series({'x': 5, 'y': 10, 'z': 15}))

def f4():
    s = pd.Series({'x': 5, 'y': 10, 'z': 15})
    print(s['y'])

def f5():
    print(df)

def f6():
    data = [
        ["Rahul", 22, "Pune"],
        ["Priya", 21, "Mumbai"],
        ["Amit", 23, "Nashik"],
        ["Neha", 22, "Delhi"]
    ]
    print(pd.DataFrame(data, columns=["Name", "Age", "City"]))

def f7():
    print(df["Name"])

def f8():
    print(df[["Name", "City"]])

def f9():
    print(df.loc[0:1])

def f10():
    print(df.iloc[2])

def f11():
    temp = df.copy()
    temp["Marks"] = [78, 85, 90, 67]
    print(temp)

def f12():
    temp = df.copy()
    temp["Course"] = ["Python", "Java", "Python", "Data Science"]
    print(temp)

def f13():
    print(df.drop("City", axis=1))

def f14():
    print(df.drop(1))

def f15():
    print(df[df["Age"] > 22])

def f16():
    print(df[df["City"] == "Pune"])

def f17():
    print(df[(df["Age"] > 21) & (df["City"] == "Delhi")])

def f18():
    csv_df = pd.read_csv("students.csv")
    print(csv_df.head(3))

def f19():
    temp = df.copy()
    temp["Marks"] = [78, 85, 90, 67]
    temp.to_csv("students.csv", index=False)
    csv_df = pd.read_csv("students.csv")
    print(csv_df[["Name", "Marks"]])

def f20():
    excel_df = pd.read_excel("students.xlsx")
    print(excel_df.head())
    print(excel_df.shape)
    print(excel_df.columns)
    print(excel_df.dtypes)

def f21():
    csv_df = pd.read_csv("students.csv")
    print(csv_df.shape)

def f22():
    temp = df.copy()
    temp["Marks"] = [78, 85, 90, 67]
    print(temp["Marks"].max())
    print(temp["Marks"].min())

def f23():
    temp = df.copy()
    temp["Marks"] = [78, 85, 90, 67]
    print(temp["Marks"].mean())

def f24():
    print(df.info())

def f25():
    missing_df = pd.DataFrame({
        "Name": ["Rahul", "Priya", None],
        "Age": [22, None, 21],
        "Marks": [90, None, None]
    })
    print(missing_df.isnull())

def f26():
    missing_df = pd.DataFrame({
        "Name": ["Rahul", "Priya", None],
        "Age": [22, None, 21],
        "Marks": [90, None, None]
    })
    print(missing_df.isnull().sum())

def f27():
    missing_df = pd.DataFrame({
        "Name": ["Rahul", "Priya", None],
        "Age": [22, None, 21],
        "Marks": [90, None, None]
    })
    print(missing_df.isnull().any())

def f28():
    missing_df = pd.DataFrame({
        "Name": ["Rahul", "Priya", None],
        "Age": [22, None, 21]
    })
    missing_df["Age"].fillna(missing_df["Age"].mean(), inplace=True)
    print(missing_df)

def f29():
    missing_df = pd.DataFrame({
        "Marks": [90, None, None]
    })
    missing_df["Marks"].fillna(0, inplace=True)
    print(missing_df)

def f30():
    missing_df = pd.DataFrame({
        "Name": ["Rahul", None],
        "Marks": [90, None]
    })
    print(missing_df.dropna())

def f31():
    print(products)

def f32():
    print(products[products["Category"] == "Electronics"])

def f33():
    print(products[products["Price"] > 10000])

def f34():
    print(products["Price"].mean())

def f35():
    print(products[products["Price"] == products["Price"].max()])

def f36():
    print(products[products["Price"] == products["Price"].min()])

def f37():
    print(products[products["Quantity"] > 7])

def f38():
    temp = products.copy()
    temp["Total_Price"] = temp["Price"] * temp["Quantity"]
    print(temp)

def f39():
    temp = products.copy()
    temp["Total_Price"] = temp["Price"] * temp["Quantity"]
    print(temp[["Product", "Total_Price"]])

def f40():
    print(products["Quantity"].sum())

print(df,"\n\n",products,"\n")
with open("Questions.txt","r",encoding="utf-8") as file:
    f=file.readlines()
for i in f:
    print(i)
func=[
    f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,
    f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,
    f21,f22,f23,f24,f25,f26,f27,f28,f29,f30,
    f31,f32,f33,f34,f35,f36,f37,f38,f39,f40
]
while True:
    choice=int(input("\nEnter number of operation: "))
    if 1<=choice<=len(func):
        print("\n",f[choice-1],"\n")
        print(func[choice-1]())
    else:
        print("Enter number in 1-40")