"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
from app.models import Property
from app.forms import PropertyForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create', methods=['POST', 'GET'])
def create():
    form = PropertyForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            bedrooms = form.bedrooms.data
            bathrooms = form.bathrooms.data
            location = form.location.data
            price = form.price.data
            property_type = form.type.data
            description = form.description.data
            photo = form.photo.data

            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.static_folder, app.config['UPLOAD_FOLDER'], filename))

            created_property = Property(title, bedrooms, bathrooms, location, price,
                                        property_type, description, filename)
            db.session.add(created_property)
            db.session.commit()

            flash('Property Added', 'success')
            return redirect(url_for('view_all'))
        flash_errors(form)

    return render_template('createProperty.html', form=form)


@app.route('/properties')
def view_all():
    image_uploads = get_photo_listing()
    upload_folder = app.config['UPLOAD_FOLDER']
    properties = db.session.execute(db.select(Property)).scalars()

    return render_template('viewProperties.html',
                           image_uploads=image_uploads,
                           properties=properties,
                           upload_folder=upload_folder
                           )

@app.route('/properties/<propertyid>')
def view_property(propertyid):
    find_property = db.get_or_404(Property, propertyid)
    upload_folder = app.config['UPLOAD_FOLDER']

    return render_template('viewProperty.html', find_property=find_property, upload_folder=upload_folder)

###
# The functions below should be applicable to all Flask apps.
###

def get_photo_listing():
    rootdir = os.getcwd()
    uploads_folder = app.config['UPLOAD_FOLDER']
    uploads_path = os.path.join(rootdir, uploads_folder)
    image_uploads = []

    if os.path.exists(uploads_path) and os.path.isdir(uploads_path):
        for subdir, dirs, files in os.walk(uploads_path):
            for file in files:
                image_uploads.append(os.path.join(subdir, file))

    return image_uploads


# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
