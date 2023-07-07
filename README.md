# BikeShop
Backend for bikeshop e-commerce website.
# API
Disclaimer: The following API is yet to be implemented and subject to change.
## Products:

* GET /products: Allow any user.
* GET /products/{id}: Allow any user.
* POST /products: Allow only admin users.
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
## Users:

* GET /users: Admin users only. Use 'show_inactive=true' to include inactive users.
* GET /users/{id}: Allow only admin users.
* POST /users: Allow only admin users.
* PUT /users/{id}: Allow only admin users.
* DELETE /users/{id}: Allow only admin users.
## Authentication and Authorization:

* POST /login: Allow any user.
* POST /logout: Allow any authenticated user.
* POST /register: Allow any user. (Needs more strict password processing)
* GET /me: Allow any authenticated user.
## Cart:
(needs permissions fixes)
* GET /cart: Allow any authenticated user.
* POST /cart: Allow any authenticated user.
* PUT /cart/{id}: Allow any authenticated user.
* DELETE /cart/{id}: Allow any authenticated user.
