from flask import Flask, render_template, request, redirect, url_for, session, flash
from decimal import Decimal
app = Flask(__name__)
app.secret_key = "change_this_to_a_random_secret_key"

# Dummy product catalog    #product1.svg
PRODUCTS = [
    {"id": 1, "name": "Classic Sneakers", "price": 69.99, "desc": "Comfortable everyday sneakers.", "image": "static/images/boot.webp"},
    {"id": 2, "name": "Leather Jacket", "price": 199.50, "desc": "Stylish leather jacket.", "image": "static/images/j.webp"},
    {"id": 3, "name": "Wireless Headphones", "price": 129.00, "desc": "Noise cancelling over-ear headphones.", "image": "static/images/Airpods.webp"},
    {"id": 4, "name": "Smart Watch", "price": 149.99, "desc": "Track your fitness and notifications.", "image": "static/images/watch.webp"}
]

def get_product(product_id):
    return next((p for p in PRODUCTS if p["id"]==product_id), None)

@app.route("/")
def home():
    return render_template("home.html", products=PRODUCTS)

@app.route("/products")
def products():
    return render_template("products.html", products=PRODUCTS)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = get_product(product_id)
    if not product:
        return redirect(url_for('products'))
    return render_template("product_detail.html", product=product)

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    # convert to list with product data and subtotal
    items = []
    total = Decimal("0.00")
    for pid, qty in cart.items():
        p = get_product(int(pid))
        if p:
            subtotal = Decimal(str(p["price"])) * int(qty)
            items.append({"product": p, "qty": qty, "subtotal": subtotal})
            total += subtotal
    return render_template("cart.html", items=items, total=total)

@app.route("/cart/add/<int:product_id>", methods=["POST","GET"])
def add_to_cart(product_id):
    qty = int(request.form.get("qty", 1))
    cart = session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + qty
    session["cart"] = cart
    flash("Item added to cart.", "success")
    return redirect(request.referrer or url_for("products"))

@app.route("/cart/update", methods=["POST"])
def update_cart():
    cart = {}
    for key, value in request.form.items():
        if key.startswith("qty_"):
            pid = key.split("_",1)[1]
            try:
                q = int(value)
            except:
                q = 0
            if q>0:
                cart[pid]=q
    session["cart"] = cart
    flash("Cart updated.", "info")
    return redirect(url_for("cart"))

@app.route("/cart/remove/<int:product_id>")
def remove_item(product_id):
    cart = session.get("cart", {})
    cart.pop(str(product_id), None)
    session["cart"] = cart
    flash("Item removed.", "warning")
    return redirect(url_for("cart"))

@app.route("/checkout", methods=["GET","POST"])
def checkout():
    if request.method=="POST":
        # pretend to process order
        session.pop("cart", None)
        flash("Order placed successfully! (demo)", "success")
        return redirect(url_for("home"))
    return render_template("checkout.html")

# Simple auth (demo only, no password hashing, do NOT use in production)
USERS = {}
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        if username in USERS:
            flash("Username already taken.", "danger")
        else:
            USERS[username]=password
            session["user"] = username
            flash("Registered and logged in.", "success")
            return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        if USERS.get(username)==password:
            session["user"]=username
            flash("Logged in.", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials.", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out.", "info")
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)
