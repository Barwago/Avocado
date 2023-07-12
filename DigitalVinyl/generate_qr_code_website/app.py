from flask import Flask, render_template, request
import qrcode
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr_code', methods=['POST'])
def generate_qr_code():
    song_url = request.form['song_url']
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(song_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("static/song_qr_code.png")

    return render_template('result.html', song_url=song_url)

if __name__ == '__main__':
    app.run()
