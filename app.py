from flask import Flask, render_template
import weather

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    location = 'Cluj-Napoca'
    app.run()
