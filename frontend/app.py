import streamlit as st
import requests
import pandas as pd


st.write("""
        # 📊 Query and execute CRUD operations within a PostgreSQL database
                 
         """)

st.write("Product Management 🔎📝⬇️")

def show_response_message(response):
    if response.status_code == 200:
        st.success("Operation succeeded")
    else:
        try:
            data = response.json()
            if "detail" in data:
                # if the error is a list extract the message from each error
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Erro: {errors}")
                else:
                    # else, shows the error message directly
                    st.error(f"Erro : {data['detail']}")
        except:
            st.error("Unknown error. We couldn't decode your answer")

# Add a new product
with st.expander("Add a new product"):
    with st.form("New Product"):
        name = st.text_input("Product's Name", key="add_name")
        description = st.text_area("Description", key="add_description")
        price = st.number_input("Price", min_value=0.01, format="%f", key="add_price")
        category = st.selectbox(
            "Category",
            ["Sports", "Fitness", "Electronics", "Food"],
            key="add_category",
        )
        email_supplier = st.text_input("Supplier's E-mail", key="add_email")
        submit_button = st.form_submit_button("Add product")

        if submit_button:
            response = requests.post(
                "http://backend:8501/products/",
                json={
                    "name": name,
                    "description": description,
                    "price": price,
                    "category": category,
                    "email_supplier": email_supplier,
                },
            )
            show_response_message(response)

# Show products
with st.expander("Show Products"):
    if st.button("Show all products", key="show_products"):
        response = requests.get("http://backend:8501/products/")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame(product)

            # structure from the models
            df = df[
                [
                    "id",
                    "name",
                    "description",
                    "price",
                    "category",
                    "email_supplier",
                    "created_at",
                ]
            ]

            # Show the Dataframe without the index
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Show product by id
with st.expander("Show Details for one product"):
    product_id = st.number_input("Product ID", min_value=1, format="%d", key="show_product_id")
    if st.button("Search Product", key="search_product"):
        response = requests.get(f"http://backend:8501/products/{product_id}")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame([product])

            df = df[
                [
                    "id",
                    "name",
                    "description",
                    "price",
                    "category",
                    "email_supplier",
                    "created_at",
                ]
            ]

            # Show the Dataframe without the index
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Delete a product
with st.expander("Delete a product"):
    delete_id = st.number_input("Product ID", min_value=1, format="%d", key="delete_product_id")
    if st.button("Delete Product", key="delete_product"):
        response = requests.delete(f"http://backend:8501/products/{delete_id}")
        show_response_message(response)

# Update a product
with st.expander("Update Product"):
    with st.form("update_product"):
        update_id = st.number_input("Product ID", min_value=1, format="%d", key="update_id")
        new_name = st.text_input("New Product's name", key="update_name")
        new_description = st.text_area("New Product's Description", key="update_description")
        new_price = st.number_input("New Product's Price", min_value=0.01, format="%f", key="update_price")
        new_category = st.selectbox(
            "New Product's Category",
            ["Sports", "Fitness", "Electronics", "Food"],
            key="update_category",
        )
        new_email_supplier = st.text_input(
            "New Product's Supplier's E-mail", key="update_email"
        )

        update_buttom = st.form_submit_button("Update Product")

        if update_buttom:
            update_data = {}
            if new_name:
                update_data["name"] = new_name
            if new_description:
                update_data["description"] = new_description
            if new_price > 0:
                update_data["price"] = new_price
            if new_category:
                update_data["category"] = new_category
            if new_email_supplier:
                update_data["email_supplier"] = new_email_supplier

            if update_data:
                response = requests.put(
                    f"http://backend:8501/products/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("We didn't find any information to update")