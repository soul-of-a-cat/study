from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
            'Присоединяйся!']
    return '</br>'.join(list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='images/MARS.jpg')}" 
                               alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
            'Присоединяйся!']
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='images/MARS.jpg')}" 
                               alt="здесь должна была быть картинка, но не нашлась"></br>
                    <p1>{list[0]}</br></p1>
                    <p2>{list[1]}</br></p2>
                    <p3>{list[2]}</br></p3>
                    <p4>{list[3]}</br></p4>
                    <p5>{list[4]}</br></p5>
                  </body>
                </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    return f"""<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style1.css')}" />
                        <title>Пример формы</title>
                    </head>
                    <body>
                        <h1 align='center', font size='5'>Анкета претендента</h1>
                        <h2 align='center', font size='4'>на участие в миссии</h2>
                        <div>
                            <form class="login_form">
                                <input type="text" class="form-control" id="surname" placeholder="Введите фамилию">
                                <input type="text" class="form-control" id="name" placeholder="Введите имя"></br>
                                <input type="text" class="form-control" id="email" placeholder="Введите адрес почты">
                                <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                </div>
                                <div class="form-group">
                                        <label for="form-check">Какие у Вас профессии?</label>
                                        <div class="form-check">
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Инженер-исследователь
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Пилот
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Строитель
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Экзобиолог
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Врач
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Инженер по терраформированию
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Климатолог
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Специалист по радиационной защите
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Астрогеолог
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Гляциолог
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Инженер жизнеобеспечения
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Метеоролог
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Оператор марсохода
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Киберинженер
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Штурман
                                            </label><br/>
                                            <input type="checkbox" name="action1" id="action1">
                                            <label for="action1">
                                                Пилот дронов
                                            </label><br/>
                                        </div>
                                </div>
                                <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                </div>
                                <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">
                                            Готовы остаться на Марсе?
                                        </label>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                    </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
