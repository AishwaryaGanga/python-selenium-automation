# Created by vaishnavisethuraman at 14/07/22
Feature: Click "Order and return" to sign in
  # Enter feature description here

  Scenario: User enters to Sign in by clicking order or return
    Given Open Amazon.com Page
    When Click order and Return tab
    Then Open amazon sign in page
    Then check email_Id space