from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data (simulated database)
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# -----------------------------
# Homepage Route
# -----------------------------


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200


# -----------------------------
# GET all products or filter
# -----------------------------
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        # Filter products by category
        filtered_products = [
            product for product in products
            if product["category"].lower() == category.lower()
        ]
        return jsonify(filtered_products), 200  # Return list directly

    # Return all products as a list
    return jsonify(products), 200


# -----------------------------
# GET product by ID
# -----------------------------
@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
