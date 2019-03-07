import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

# указываем папку, в которую будут загружаться файлы
UPLOAD_FOLDER = 'C:/UploFiles'
# указываем допустимые расширения
ALLOWED_EXTENSIONS = set(['txt', 'fb2'])

# указываем класс name, чтобы фласк понимал, с чем мы работаем
app = Flask(__name__)
# указываем фласку на папку, заданную нами ранее
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# проверяем соответствует ли расширение файла разрешенным
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# указываем url который будет вызывать функцию, в нашем случае это стартовая страница "/"
@app.route('/', methods=['GET', 'POST'])
# request method  POST нужен для того чтобы загружать файлы
def upload_file():
    print(request.files)
    if request.method == 'POST':
        # указываем что такое file, у нас file это то, что сайт запрашивает у юзера
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # сохраняем в выбранную папку под оригинальным именем 'filename'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('file_uploaded.html')
    return render_template('upload_file.html')

app.run(debug=True)
