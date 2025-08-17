import pandas as pd
from bs4 import BeautifulSoup
import streamlit as st
from io import BytesIO
import requests

def scrape_books():
    url="https://books.toscrape.com/"
    response=requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    #print(soup)
    books=[]
    
    for article in soup.find_all('article', class_="product_pod"):
        title = article.h3.a["title"]
        price = article.find("div", class_="product_price").find("p", class_="price_color").text
        availability = article.find("div", class_="product_price").find("p", class_="instock availability").text.strip()
        books.append({
            "Title": title,
            "Price": price,
            "available": availability
        })
    return books

st.header("Book scraping")

if st.button("Scrape books"):
    with st.spinner("Getting book data..."):

        df=scrape_books()
        st.dataframe(df)
        st.success("Successfully scraped books!")
        # Convert DataFrame to CSV
        csv_buffer = BytesIO()
        # Create an in-memory buffer for binary data. We’ll write the CSV there instead of writing a file to disk.
        df = pd.DataFrame(df)
        df.to_csv(csv_buffer, index=False)
        # Write the DataFrame to the BytesIO buffer in CSV format. index=False tells pandas not to write the DataFrame index
        # as a separate column (keeps file neat).
        # pandas will encode the CSV text into bytes when writing to a BytesIO.
        csv_data = csv_buffer.getvalue()
        # Get the contents of the buffer as raw bytes — ready to pass to st.download_button (which accepts bytes, str, or file-like objects).

        # Download button
        st.download_button(
            label="📥 Download CSV",
            data=csv_data,
            file_name="books_data.csv",
            mime="text/csv"
        )