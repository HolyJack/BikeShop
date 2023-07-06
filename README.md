# BikeShop
Backend for bikeshop e-commerce website.
# API
Disclaimer: The following API is yet to be implemented and subject to change.
## Products:

* GET /products: Allow any authenticated user (IsAuthenticated).
* GET /products/{id}: Allow any authenticated user.
* POST /products: Allow only admin users (IsAdminUser).
* PUT /products/{id}: Allow only admin users.
* DELETE /products/{id}: Allow only admin users.
## Categories:

* GET /categories: Allow any authenticated user.
* GET /categories/{id}: Allow any authenticated user.
* POST /categories: Allow only admin users.
* PUT /categories/{id}: Allow only admin users.
* DELETE /categories/{id}: Allow only admin users.
## Orders:

* GET /orders: Allow only admin users.
* GET /orders/{id}: Allow only admin users.
* POST /orders: Allow any authenticated user.
* PUT /orders/{id}: Allow only admin users.
* DELETE /orders/{id}: Allow only admin users.
## Customers:

* GET /customers: Allow only admin users.
* GET /customers/{id}: Allow only admin users.
* POST /customers: Allow any authenticated user.
* PUT /customers/{id}: Allow only admin users.
* DELETE /customers/{id}: Allow only admin users.
## Reviews:

* GET /products/{id}/reviews: Allow any authenticated user.
* GET /reviews/{id}: Allow any authenticated user.
* POST /products/{id}/reviews: Allow any authenticated user.
* PUT /reviews/{id}: Allow only the author of the review or admin users.
* DELETE /reviews/{id}: Allow only the author of the review or admin users.
## Authentication and Authorization:

* POST /login: Allow any user.
* POST /logout: Allow any authenticated user.
* POST /register: Allow any user.
* GET /me: Allow any authenticated user.
## Cart:

* GET /cart: Allow any authenticated user.
* POST /cart: Allow any authenticated user.
* PUT /cart/{id}: Allow any authenticated user.
* DELETE /cart/{id}: Allow any authenticated user.
