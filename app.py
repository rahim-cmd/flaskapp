from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def home():
    title="home"
    return render_template('index.html',title=title)
@app.route("/about")
def about():
    title="About"
    return render_template('about.html',title=title)
@app.route("/contact")
def contact():
    title="Contact"
    return render_template('contact.html',title=title)
@app.route("/services")
def service():
    title="service"
    return render_template('service.html',title=title)
@app.route("/project")
def project():
    title="project"
    return render_template('project.html',title=title)
@app.route("/feature")
def feature():
    title="feature"
    return render_template('feature.html',title=title)
@app.route("/blog")
def blog():
    title="blog"
    return render_template('blog.html',title=title)
@app.route("/team")
def team():
    title="team"
    return render_template('team.html',title=title)
@app.route("/testimonial")
def testimonial():
    title="testimonial"
    return render_template('testimonial.html',title=title)
@app.route("/404")
def four():
    title="404"
    return render_template('404.html',title=title)

app.run(debug='false')


