from flask import Flask
import random


app = Flask(__name__)
gif_list = ['https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmJiMWMxMDMxMGYyZjNkZTllOTQwNzFhN2Q4NDNiYmIyMzA4Y2U1OSZjdD1n/NpL4D3Oc2bJUMAXF9P/giphy.gif',
            'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGZhZGUzNzlhOTJhZDk0ZmUxNTZlOTdiYWVhYzBiZjU4MTZlYmJjOCZjdD1n/CWN0uW6ELn3pK/giphy.gif',
            'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGNkMGQ5OTc1MDE3ZGVhYzYwYzdiODMyMTcxNzUzNWU0OTk3OThiOCZjdD1n/ySlraQoZhmeUskuOX5/giphy.gif',
            'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmE4Y2JhYTNjMDYyNDhmODZmNGQ2NDM5YWRhYWVjNGNjOGFjOGEzNSZjdD1n/4cuyucPeVWbNS/giphy.gif',
            'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDYwNjRjNmQ2NzhjZmZjMzk5ZDFiMjFmMGE4YTg2ZjFkY2Y3MjU0MyZjdD1n/ljtfkyTD3PIUZaKWRi/giphy.gif',
            'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2FkNTg1NjQ0ZmExYjZkODUxZGU0OTAxZGEzZDY0ODQ4YWY2YTZkOCZjdD1n/hyyV7pnbE0FqLNBAzs/giphy.gif']
rand = random.randrange(10)
print(rand)


@app.route('/')
def index():
    return f"<h1>Guess a number between 0 and 9.</h1><br><img src='https://media.giphy.com/media/BpGWitbFZflfSUYuZ9/giphy.gif'>"


@app.route('/<num>')
def guess(num):
    rand_gif = random.randrange(6)
    picked_rand_gif = gif_list[rand_gif]
    if int(num) == int(rand):
        return f"<h1 style='color:green;'>That's correct! {num} is the correct number!</h1><br><img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjg5YTI5MmVmYTZkMTE0ZDI3MGZkZDNmNjRjNmE5OGZhYjhiMmI0NiZjdD1n/ynRrAHj5SWAu8RA002/giphy.gif'>"
    elif int(num) > int(rand):
        return f"<h1 style='color:red;'>To High!!!!</h1><br><img src='{picked_rand_gif}'>"
    else:
        return f"<h1 style='color:blue;'>To Low!!!!</h1><br><img src='{picked_rand_gif}'>"


if __name__ == '__main__':
    app.run()
