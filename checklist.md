## Checklist for automation testing UI: Online Shop
This checklist outlines the automated UI tests for a web online shop. 
Tests provide smoke testing with a set of checks for standard user actions. 
The goal of these tests is to ensure the correct functioning of the online shop and 
provide a seamless user experience.

### 1. Authorization and Access to the Product Catalog:
- Enter correct login and password, verify successful authorization.
- Enter incorrect login and password, verify error message.

### 2. Product Sorting:
- Apply sorting by price (from low to high).
- Verify that products are displayed in the correct order.

### 3. Adding Two Products to Cart and Checking its Contents:
- Select the cheapest product (1st on the page) and add it to the cart.
- Select the 4th product on the page and add it to the cart.
- Open the cart and verify the presence of the two added products.
- Verify the correctness of displaying the product names and prices.
  
  Note: Since products in the catalog can be removed or new ones can appear, 
  the tests are designed in a way that the added products can change manually in the code.
  To do this, you need to change their numbers in the location on the page.

### 4. Confirmation and Complete the Order:
- Enter customer information and proceed to the order confirmation page.
- Verify that the names of the added products match on the order confirmation page.
- Verify that the total amount of the added products is calculated correctly.
- Complete the checkout process and verify successful order placement.





    