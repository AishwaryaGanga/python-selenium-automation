# Created by vaishnavisethuraman at 15/07/22
Feature: Add a product to cart

  Scenario: Users adds product to cart.
    Given Open Amazon Page
    When Click search for Harry Potter books set on product
    When Click on the book
    When Add the product to cart
    Then Check the cart for product