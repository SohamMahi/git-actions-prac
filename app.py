# This is Flask Code
from flask import Flask, render_template
app = Flask(_name_)

@app.route('/')
  def hello_world():
      return render_template('index.html')

@app.route('/health')
  def health():
      return 'Server is Up and Running'
