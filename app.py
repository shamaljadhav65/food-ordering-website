from flask import Flask, render_template

app = Flask(__name__)

menu_categories = {
    "Starters": [
        {"name": "Paneer Tikka", "price": "₹250", "image": "https://images.unsplash.com/photo-1628294895950-9805252327bc?auto=format&fit=crop&w=400&q=80"},
        {"name": "Samosa Chaat", "price": "₹120", "image": "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=400&q=80"},
        {"name": "Hara Bhara Kabab", "price": "₹200", "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=400&q=80"}
    ],
    "Main Course": [
        {"name": "Butter Chicken", "price": "₹350", "image": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=400&q=80"},
        {"name": "Dal Makhani", "price": "₹220", "image": "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=400&q=80"},
        {"name": "Hyderabadi Biryani", "price": "₹320", "image": "https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?auto=format&fit=crop&w=400&q=80"}
    ],
    "Desserts & Beverages": [
        {"name": "Gulab Jamun", "price": "₹100", "image": "https://images.unsplash.com/photo-1598514982205-f36b96d1e8d4?auto=format&fit=crop&w=400&q=80"},
        {"name": "Mango Lassi", "price": "₹90", "image": "https://images.unsplash.com/photo-1570696516188-ade861b84a49?auto=format&fit=crop&w=400&q=80"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_categories=menu_categories)

@app.route('/about')
def about():
    return render_template('about.html')

# New Cart Route
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
