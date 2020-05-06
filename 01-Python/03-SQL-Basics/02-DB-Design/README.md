## Background & Objectives

The goal of this first challenge is to become familiar with database design,
*a* crucial skill to make your backend maintainable, flexible and efficient.

## Specs

#### E-commerce database design

There are many ways to build an e-commerce database, but let's start by building a basic
system with `customers`, `products` and `orders`.

Here are the requirements of our system:

- A customer has a `first_name`, `last_name`, an `email` and a `city`,
- A product has a `name` and a `unit_price`.
- An order is defined by a `date_of_order`.
- The e-commerce manages several `customers`.
- A customer can make many `orders`, but an order is created by only one user.
- A order can have several `products`.
- A product can be in different `orders`.


#### Design the schema

Design a database schema for an e-commerce app that meets the requirements.
For this, you must use the [SQL Designer](http://db.lewagon.com).
To check your solution, click on "Save / Load", then "Save XML", copy/paste the generated XML code
in `ecommerce.xml`. You can then `make` to check your solution.

## Key learning points

- Do you know what a schema is?
- What's the relation between tables?
- Could you draw the database schema behind facebook? airbnb? Take a sheet of paper and have a go!
