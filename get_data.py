import requests

url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/winequality-white.csv"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    with open("winequality-white.csv", "wb") as f:
        f.write(response.content)
    print("Dataset downloaded successfully.")
else:
    print("Failed to download dataset.")