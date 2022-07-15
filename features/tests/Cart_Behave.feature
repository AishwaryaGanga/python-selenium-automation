# Created by vaishnavisethuraman at 14/07/22
Feature: To check amazon cart
  # Enter feature description here

  Scenario: To check amazon cart is empty when clicked
  Given Open amazon.com page1
  When Click on the cart icon
  Then Verify your amazon cart is empty
