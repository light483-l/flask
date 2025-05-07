from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    promotion_list = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '<br>'.join(promotion_list)


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='13.png')}">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <title>Промо Марс</title>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                    <div class="container mt-5">
                      <h1 class="promo-title">Жди нас, Марс!</h1>
                      <img src="{url_for('static', filename='img/13.png')}" class="promo-image img-fluid">
                      <div class="promo-items">
                        <div class="promo-item item-1">Человечество вырастает из детства.</div>
                        <div class="promo-item item-2">Человечеству мала одна планета.</div>
                        <div class="promo-item item-3">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <div class="promo-item item-4">И начнем с Марса!</div>
                        <div class="promo-item item-5">Присоединяйся!</div>
                      </div>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
