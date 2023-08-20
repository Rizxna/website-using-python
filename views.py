from flask import Flask, request ,render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField
from wtforms.validators import DataRequired, Email , Length ,  EqualTo
import os
from datetime import datetime



app = Flask(__name__)
app.secret_key="hey its me Rizwana"

categories = ["Game", "Technical", "Story", "Books", "Real world", "Others"]

projects = []


 
@app.route("/livestreams")
def livestreams():
    return render_template('video_updates.html' , livestreams = True)


@app.route("/analytics")
def analytics():
    return render_template("analytics.html",analytics=True)

class LoginForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")



@app.route("/login", methods=['GET','POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        email=form.email.data
        password=form.password.data
    return render_template("login.html", form=form, login=True)

class SignupForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    submit = SubmitField("Register Now")

@app.route("/signup", methods=['GET'])
def signup_form():
    form=SignupForm()
    return render_template("signup.html", form=form, signup_form=True)

@app.route("/signup", methods=['POST'])
def signup_submit():
    return redirect(url_for('home'))


@app.route("/support")
def support():
    return render_template("support.html",support=True)

@app.route("/about")
def about():
    return render_template("about.html", products=products)

@app.route("/createproject", methods=['GET','POST'])
def create_project():
    if request.method == 'POST':
        project = {
            'title': request.form['title'],
            'description': request.form['description'],
            'funding_goal': float(request.form['funding_goal']),
            'funding_tiers': [],
            'category': request.form['category'],
            'resources': request.form['resources'],
            'stretch_goals': request.form['stretch_goals'],
            'start_date': datetime.strptime(request.form['start_date'], '%Y-%m-%dT%H:%M'),
            'end_date': datetime.strptime(request.form['end_date'], '%Y-%m-%dT%H:%M'),
            'images': [],
        }

        for i in range(1, 5):
            price = float(request.form[f'price_{i}'])
            reward = request.form[f'reward_{i}']
            image = request.files.get(f'image_{i}')

            if price and reward and image:
                project['funding_tiers'].append({
                    'price': price,
                    'reward': reward,
                    'image': image.filename
                })

                image.save(os.path.join('static', 'images', image.filename))
                project['images'].append(image.filename)

        projects.append(project)
        flash('Project created successfully', 'success')
        return redirect('/')

    return render_template('createproject.html', categories=categories )


@app.route('/yourproject')
def yourproject():
    return render_template('displayprojects.html', projects=projects)

@app.route("/allprojects")
def allprojects():
    return render_template("allprojects.html", products=products)

@app.route("/category")
def category():
    return render_template("category.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/marketplace")
def marketplace():
    return render_template("marketplace.html", products= products)

@app.route("/search")
def search():
    return render_template("search.html")

@app.route('/profile')
def profile():
    user = {
        'first_name': 'Rizwana',
        'last_name': 'Rasheed',
        'bio': 'A passionate creator and supporter of amazing projects!',
        'created_projects': [
            {'title': 'Project 1'},
            {'title': 'Project 2'},
            # Add more projects
        ],
        'backed_projects': [
            {'title': 'Project A'},
            {'title': 'Project B'},
            # Add more projects
        ]
    }
    return render_template("profile.html", user=user)

@app.route('/profileedit', methods=['POST'])
def edit_profile():
    new_first_name = request.form['new_first_name']
    new_last_name = request.form['new_last_name']
    new_bio = request.form['new_bio']
    new_email = request.form['new_email']
    new_password = request.form['new_password']

    # Update the user's profile information in your data store
    # You might want to use a database query or similar method here

    flash('Profile updated successfully!', 'success')
    return redirect(url_for('profile'))

@app.route('/')
def home():
    print("Recommended Projects:", recommended_projects)
    print("Featured Projects:", featured_projects)
    return render_template('home.html', recommended_projects=recommended_projects, featured_projects=featured_projects, home=True)




@app.route('/project/<int:project_id>')
def project_details(project_id):
    project = {
        'id': project_id,
        'title': f'project {project_id}',
        'image': f'project{project_id}',
        'description': f'Description of project{project_id}',
        'funds_raised': f'${project_id * 1000}',
        'is_saved': False,
        'is_bookmarked': True
    }
    return render_template('projectdetails.html', project=project)

recommended_projects = [
    {
        'id': 1,
        'title': 'GENSHIN IMPACT 4.0 IS OUT NOW',
        'description': 'Experience our new feature of Diving and take part in the thrilling crime solving mystery case now',
        'image': 'gi9.jpg'
    }
    # Add more recommended projects
]

featured_projects = [
    {
        'id': 2,
        'title': 'Honkai Star Rail',
        'description': 'Try this turn-based game and enjoy',
        'image': 'hsr2.jpg'
    },
    {
        'id': 3,
        'title': 'shoe painting',
        'description': 'Make your plain shoes more beautiful with amazing paintings',
        'image': 'shoe3.jpg'
    },
    {
        'id': 4,
        'title': 'Read our new volume',
        'description': 'The new volume is out, Now immerse yourself into this adventurous world',
        'image': 'book1.jpg'
    },
    # Add more featured projects
]

def update_like_count(project_id):
    print(f'Updates like count for project (project_id)')

@app.route('/like_project/<int:project_id>')
def like_project(project_id):
    update_like_count(project_id)
    return render_template('home.html', recommended_projects=recommended_projects, featured_projects=featured_projects)

# Route to handle bookmarking a project
@app.route('/bookmark_project/<int:project_id>')
def bookmark_project(project_id):
    # Add the project to the user's bookmarks in your data store
    # Redirect back to the home page or project list
    return redirect(url_for('profile'))

profile_data = {
    'email': 'usercreator@example.com',
    'firstName': 'Rizwana',
    'lastName': 'Rasheed',
    'address1': 'xyz Main Street',
    'address2': ' near abc',
    'zipcode': '000000',
    'city': 'Dubai',
    'state': 'DUBAI',
    'country': 'UAE',
    'phone': '123-456-7890'
    'bookmarked projects : Projects'
}

@app.route('/profileedit', methods=['GET', 'POST'])
def profileedit():
    if request.method == 'POST':
        # Update the profile data based on the form input
        profile_data['firstName'] = request.form['firstName']
        profile_data['lastName'] = request.form['lastName']
        profile_data['address1'] = request.form['address1']
        profile_data['address2'] = request.form['address2']
        profile_data['zipcode'] = request.form['zipcode']
        profile_data['city'] = request.form['city']
        profile_data['state'] = request.form['state']
        profile_data['country'] = request.form['country']
        profile_data['phone'] = request.form['phone']

        # Redirect to profile page after updating
        return redirect(url_for('profileedit'))

    return render_template('profileedit.html', profileData=profile_data)


if __name__ == '__main__':
    app.run(debug=True)

