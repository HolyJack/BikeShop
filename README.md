# BikeShop
Backend for bikeshop e-commerce website.
# API
Disclaimer: The following API is implemented but could be subject to change.
## Products:

* GET /api/products: Allow any user.
* GET /api/products/{id}: Allow any user.
* POST /api/products: Allow only admin users.
* PUT /api/products/{id}: Allow only admin users.
* DELETE /api/products/{id}: Allow only admin users.
## Categories:

* GET /api/categories: Allow any authenticated user.
* GET /api/categories/{id}: Allow any authenticated user.
* POST /api/categories: Allow only admin users.
* PUT /api/categories/{id}: Allow only admin users.
* DELETE /api/categories/{id}: Allow only admin users.
## Orders:

* GET /api/orders: Allow only admin users. 
* GET /api/orders/{id}: Allow only admin users. 
* POST /api/orders: Allow any authenticated user. 
* PUT /api/orders/{id}: Allow only admin users. 
* DELETE /api/orders/{id}: Allow only admin users. 
## Users:

* GET /api/users: Admin users only. Use 'show_inactive=true' to include inactive users.
* GET /api/users/{id}: Allow only admin users.
* POST /api/users: Allow only admin users.
* PUT /api/users/{id}: Allow only admin users.
* DELETE /api/users/{id}: Allow only admin users.
## Authentication and Authorization:

* POST /api/login: Allow any user.
* POST /api/logout: Allow any authenticated user.
* POST /api/register: Allow any user. (Needs more strict password processing)
* GET /api/me: Allow any authenticated user.
## Cart:
(needs permissions fixes)
* GET /cart: Allow any authenticated user.
* POST /cart: Allow any authenticated user.
* PUT /cart/{id}: Allow any authenticated user.
* DELETE /cart/{id}: Allow any authenticated user.
