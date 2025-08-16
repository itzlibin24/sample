from flask import Flask, render_template, url_for, send_from_directory, abort
import os

app = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images')

@app.route('/')
def gallery():
    image_filenames = [
        f for f in os.listdir(IMAGE_FOLDER)
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    return render_template('gallery.html', images=image_filenames)

@app.route('/image/<filename>')
def image_page(filename):
    file_path = os.path.join(IMAGE_FOLDER, filename)
    if not os.path.exists(file_path):
        abort(404)
    image_url = url_for('static', filename=f'images/{filename}')
    return render_template('image_page.html', filename=filename, image_url=image_url)

@app.route('/download/<filename>')
def download_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
