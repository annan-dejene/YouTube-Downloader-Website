from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from youtube_downloder import downloader


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hawisecretbeki'


@app.route('/', methods=['GET','POST'])
def index():
  if request.method == 'POST':
    url = request.form['url']
    cat, buffer, fname = downloader(url)
    if cat == 'Success':
      flash('Download Successful!', category='success')
      response = send_file(buffer, as_attachment=True, download_name=fname)
      return response
    else:
      flash('Download Failed!', category='error')
  
  return render_template('index.html')



@app.route('/success')
def success():
  return render_template('success.html')


@app.route('/error')
def error():
  return render_template('error.html')


if __name__ == '__main__':
  app.run(debug=True)
