# Created by vaishnavisethuraman at 25/07/22
Feature: Test a page with product name and image

  Scenario: Check product image and name.
    Given Open the search result page.
    Then Verify has a product name.
    Then Verify has a image of the products.
    Then Check block has name and image.
