from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def myhome():
    return render_template('index.html')  

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)  







# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/project.html')
# def project():
#     return render_template('project.html')
