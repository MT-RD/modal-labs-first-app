import modal

app = modal.App("first-app-get-started")

@app.function()
def square(x):
    print("This code is running on a remote worker! ")
    return x**2

@app.local_entrypoint()
def main():
    print("The square is", square.remote(42))
    