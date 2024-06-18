import pandas as pd
import re

# Example phone lists
amazon_phones = [
    {'iPhone 15 (128 GB) - Black': 73100},
    {'iPhone 13 (128GB) - Midnight': 52090},
    {'iPhone 13 (128GB) - Starlight': 52090},
    {'iPhone 13 (128GB) - Pink': 52090},
    {'iPhone 13 (128GB) - Blue': 52090},
    {'iPhone 13 (128GB) - Midnight': 52090},
    {'iPhone 13 (128GB) - Green': 52090},
    {'iPhone 15 (128 GB) - Black': 73100},
    {'iPhone 14 (128 GB) - Blue': 62800},
    {'Original Smartphone Compatible with Apple iPhone 6 Gold (64GB Storage with 1-Year Warranty)': 16999},
    {'iPhone 15 (128 GB) - Blue': 73100},
    {'Original Smartphone Compatible with Apple iPhone 5 SE Grey (16GB Storage with 1-Year Warranty)': 11999},
    {'iPhone 14 (128 GB) - Purple': 62800},
    {'iPhone 15 Plus (128 GB) - Black': 82600},
    {'iPhone 13 (256GB) - Midnight': 61390},
    {'iPhone 14 (128 GB) - Midnight': 62800},
    {'iPhone 14 (128 GB) - Starlight': 62800},
    {'iPhone 13 (256GB) - Starlight': 59900}
]

flipkart_phones = [
    {'Apple iPhone 14 Plus (Starlight, 128 GB)': 61999},
    {'Apple iPhone 14 Plus (Blue, 128 GB)': 61999},
    {'Apple iPhone 14 Plus (Purple, 128 GB)': 61999},
    {'Apple iPhone 14 Plus (Midnight, 128 GB)': 61999},
    {'Apple iPhone 15 (Blue, 128 GB)': 71499},
    {'Apple iPhone 14 Plus (Yellow, 128 GB)': 61999},
    {'Apple iPhone 15 (Black, 128 GB)': 71499},
    {'Apple iPhone 14 Plus (Midnight, 256 GB)': 71999},
    {'Apple iPhone 14 Plus ((PRODUCT)RED, 128 GB)': 61999},
    {'Apple iPhone 14 Plus (Purple, 256 GB)': 71999},
    {'Apple iPhone 14 (Blue, 128 GB)': 57999},
    {'Apple iPhone 14 Plus (Starlight, 256 GB)': 71999},
    {'Apple iPhone 15 (Green, 128 GB)': 71499},
    {'Apple iPhone 15 (Pink, 128 GB)': 71499},
    {'Apple iPhone 15 (Blue, 256 GB)': 81499},
    {'Apple iPhone 12 (Black, 64 GB)': 39999},
    {'Apple iPhone 15 Plus (Green, 128 GB)': 82499},
    {'Apple iPhone 14 Plus (Yellow, 256 GB)': 71999},
    {'Apple iPhone 14 Plus (Blue, 256 GB)': 71999},
    {'Apple iPhone 15 Plus (Blue, 128 GB)': 82499},
    {'Apple iPhone 15 (Green, 256 GB)': 81499},
    {'Apple iPhone 15 (Yellow, 128 GB)': 71499},
    {'Apple iPhone 14 Plus ((PRODUCT)RED, 256 GB)': 71999},
    {'Apple iPhone 13 (Starlight, 128 GB)': 53999}
]


# Normalize phone names for better comparison
def normalize_name(name):
    return re.sub(r'\W+', ' ', name).strip().lower()


# Function to find the best match for a phone name in a list of phones
def find_best_match(phone_name, phone_list):
    normalized_name = normalize_name(phone_name)
    best_match = None
    best_match_score = 0
    for phone in phone_list:
        for name in phone.keys():
            normalized_list_name = normalize_name(name)
            # Calculate a simple match score based on common substrings
            match_score = len(set(normalized_name.split()) & set(normalized_list_name.split()))
            if match_score > best_match_score:
                best_match = (name, phone[name])
                best_match_score = match_score
    return best_match


# Create a DataFrame for the comparisons
comparison_data = []

for amazon_phone in amazon_phones:
    for amazon_name, amazon_price in amazon_phone.items():
        best_match = find_best_match(amazon_name, flipkart_phones)
        if best_match:
            flipkart_name, flipkart_price = best_match
            price_difference = flipkart_price - amazon_price
            comparison_data.append([amazon_name, amazon_price, flipkart_name, flipkart_price, price_difference])

# Convert the comparison data into a DataFrame
df = pd.DataFrame(comparison_data,
                  columns=['Amazon Phone', 'Amazon Price', 'Flipkart Phone', 'Flipkart Price', 'Price Difference'])

# Save the DataFrame to an Excel file
df.to_excel('phone_price_comparison1.xlsx', index=False)

print("Comparison data has been saved to phone_price_comparison.xlsx")
