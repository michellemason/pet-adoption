from flask import Flask, request, render_template,  redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def list_pets():
    """List of all pets on homepage"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add')
def add_pet_form():
    """Renders the add pet form """
    form = AddPetForm()
    return render_template('add_pet_form.html', form=form)

@app.route('/add', methods=["POST"])
def handle_adding_pet():
    """Handles the form submission of new pet"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} added successfully!")
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>')
def pet_info_edit(pet_id):
    """Display info about a pet & edit form"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    return render_template('pet_info_edit.html', pet=pet, form=form)

@app.route('/<int:pet_id>', methods=["POST"])
def handle_edit_info(pet_id):
    """Handle the edit form for pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    if form.validate_on_submit():
        pet.photo = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect('/')
    else:
        return render_template('pet_info_edit.html', pet=pet, form=form)






