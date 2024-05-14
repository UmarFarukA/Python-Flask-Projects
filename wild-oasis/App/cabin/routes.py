from App.extension import (Blueprint, render_template, redirect, request, 
                           flash, url_for, login_required, jsonify)
from App.cabin.forms import AddCabinForm, EditCabinForm
from App.models.cabin import Cabin
from utils import image_name

cabin = Blueprint("cabin", __name__)

@cabin.route("/cabins", methods=["GET"])
@login_required
def index():

    form = AddCabinForm()
    page = request.args.get("page", 1, type = int)
    per_page = 10

    # Getting a paginated results
    cabins = Cabin.query.paginate(page=page, per_page=per_page)
    # for cabin in cabins:
    #     print(cabin)

    return render_template("cabin/index.html", cabins = cabins, form = form)


@cabin.route("/add", methods=["GET", "POST"])
@login_required
def create():
    """This route returns the add cabin form and add new cabin"""
    addForm = AddCabinForm(request.form)
    if  addForm.validate_on_submit():
        name = request.form['name']
        maxCapacity = request.form['maxCapacity']
        price = request.form['price']
        discount = request.form['discount']
        image = "cabin_default.png"
        
        if discount >= price:
            # flash("Discount must be less than the price of cabin", "error")
            # return redirect(url_for("cabin.index"))
            return False
        
        if "image" in request.files:
            image = image_name("cabin.create", image="image")
        
        new_cabin = Cabin(name, maxCapacity, price, discount, image)

        new_cabin.insert()
        return jsonify({"success": True, "redirect_url": url_for("cabin.index")})

    return render_template("cabin/create.html", form=addForm)


@cabin.route("/edit/<cabinId>", methods=["GET", "POST"])
@login_required
def edit_cabin(cabinId):
    """This route returns template for editing and Updating cabin"""
    editForm = EditCabinForm(request.form)

    if editForm.validate_on_submit():

        cabin_to_edit = Cabin.query.get(cabinId)

        if not cabin_to_edit:
            flash(f"No cabin with id {cabinId} exists", "error")
            return redirect(url_for("cabin.index"))
        
        cabin_to_edit.name = editForm.name.data
        cabin_to_edit.maxCapacity = editForm.maxCapacity.data
        cabin_to_edit.price = editForm.price.data
        cabin_to_edit.discount = editForm.discount.data

        cabin_to_edit.update()

        flash("Cabin successfully updated", "success")

        return redirect(url_for("cabin.index"))


    return render_template("cabin/update.html", editForm = editForm)

@cabin.route("/delete/<cabinId>", methods=["GET", "POST"])
@login_required
def delete_cabin(cabinId):
    """This route deletes a cabin base on it Id"""
    cabin_to_delete = Cabin.query.get(cabinId)

    if  not cabin_to_delete:
        flash(f"No cabin with id {cabinId} exists", "error")
        return redirect(url_for("cabin.index"))
    
    cabin_to_delete.delete()

    flash("Cabin successfully deleted", "success")

    return redirect(url_for("cabin.index"))