import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

invoices = pd.read_sql("SELECT CustomerId, Total FROM invoices", conn)
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM customers", conn)

customer_spending = (
    invoices.groupby("CustomerId")["Total"].sum().reset_index(name="TotalSpent")
)

customer_spending = customer_spending.merge(customers, on="CustomerId")

top5 = customer_spending.sort_values("TotalSpent", ascending=False).head(5)
print("Top 5 Customers by Spending:\n", top5)



invoice_items = pd.read_sql("SELECT InvoiceId, TrackId FROM invoice_items", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM tracks", conn)

purchases = invoice_items.merge(tracks, on="TrackId")

invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM invoices", conn)
cust_album = purchases.merge(invoices, on="InvoiceId")
cust_album_counts = cust_album.groupby(["CustomerId", "AlbumId"]).size().reset_index(name="BoughtTracks")

album_counts = tracks.groupby("AlbumId").size().reset_index(name="TotalTracks")

cust_album_counts = cust_album_counts.merge(album_counts, on="AlbumId")
cust_album_counts["FullAlbum"] = cust_album_counts["BoughtTracks"] == cust_album_counts["TotalTracks"]

pref = cust_album_counts.groupby("CustomerId")["FullAlbum"].any().reset_index()
pref["Preference"] = pref["FullAlbum"].apply(lambda x: "Full Album" if x else "Individual Tracks")

summary = pref["Preference"].value_counts(normalize=True) * 100
print("\nCustomer Purchase Preference (%):\n", summary)

conn.close()
