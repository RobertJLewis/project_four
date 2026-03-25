## Testing Overview

This document outlines the testing strategy, process, and results for **Project 4 – Food E-Commerce Store**. It verifies that the application’s core functionality operates correctly, delivers a responsive and accessible user experience, and meets the acceptance criteria defined by the project’s user stories and feature plan.

Testing was carried out throughout development using both **manual and automated approaches**, covering functionality, responsiveness, browser compatibility, accessibility, and data validation. Django’s built-in testing framework was used for backend validation, while real devices and browser developer tools were used to assess front-end behaviour.

This file includes:

- **User story-based test cases**  
- **Manual testing** across devices and browsers  
- **Automated unit tests** (Django models, views, and forms)  
- **Validation testing** (HTML, CSS, Python, and accessibility)  
- **Bug tracking and resolution**  
- **Known issues and limitations (if applicable)**  




## Table of Contents

1. [Validation Testing](#validation-testing)
2. [Automated Testing](#automated-testing)
3. [Manual Testing](#manual-testing)
   - [Full Application Testing](#full-application-testing)
   - [Browser Compatibility](#browser-compatibility)
   - [Responsiveness](#responsiveness)
   - [Accessibility](#accessibility)
   - [User Story Testing](#user-story-testing)
   - [Feature Testing](#feature-testing)
   - [Manual Feature Testing](#manual-feature-testing)
4. [Issues & Bug Tracking](#issues--bug-tracking)
   - [Resolved Issues](#resolved-issues)
   - [Known Issues](#known-issues)
5. [Conclusion](#conclusion)



## Testing Approach

Testing was a critical part of the **Project 4 – Food E-Commerce Store** development workflow, ensuring the application remained robust, responsive, and user-friendly throughout each stage of development. Continuous testing enabled early identification and resolution of issues, improving both development efficiency and overall site reliability.

A range of tools and methods were used to validate the application’s functionality and presentation. **Chrome Developer Tools** were used extensively to test responsiveness, inspect layout behaviour, debug JavaScript interactions, and evaluate performance across different viewport sizes. These tools were essential for refining the user experience across devices.

Throughout the project, **ChatGPT** was used to support testing strategies, clarify Django logic, refine user flows, and improve the accessibility and clarity of interface elements. This contributed to more maintainable, production-ready code and supported structured problem-solving during debugging.

To ensure the application is fully responsive and accessible, all pages and interactive elements were manually tested using Chrome’s responsive design mode, as well as on physical devices including desktops, laptops, tablets, and smartphones. Key user journeys—such as browsing products, adding items to the cart, and completing the checkout process—were tested across multiple screen sizes to ensure a seamless and consistent experience for all users.





## Validation Testing

### W3C Markup Validation

The **W3C Markup Validation Service** was used to validate the HTML output across all key pages of **Project 4 – Food E-Commerce Store**. 

As the project uses Django templates with dynamic content and template tags (e.g. `{% %}`, `{{ }}`), validation was performed on the fully rendered HTML by copying the page source from the browser into the validator. This ensures the final output—what users and browsers actually receive—complies with **HTML5 standards**.

| Page Tested        | Result | Evidence |
|-------------------|--------|----------|
| Home              | Pass   | Home Page Validation |
| All Products      | Pass   | Products Page Validation |
| Product Detail    | Pass   | Product Detail Validation |
| Cart              | Pass   | Cart Page Validation |
| Checkout          | Pass   | Checkout Page Validation |
| Checkout Success  | Pass   | Checkout Success Validation |
| Login/Register    | Pass   | Authentication Page Validation |
| Order Confirmation| Pass   | Order Confirmation Validation |
| 400 Error Page    | Pass   | 400 Page Validation |
| 403 Error Page    | Pass   | 403 Page Validation |
| 404 Error Page    | Pass   | 404 Page Validation |
| 500 Error Page    | Pass   | 500 Page Validation |

> All tested pages successfully passed validation with no critical errors, confirming compliance with modern web standards and ensuring consistent rendering across browsers.








































# TESTING

## Overview

This document outlines the testing carried out on the Full Stack web application to ensure that all features function as intended. Testing focused primarily on manual testing of core functionality, user interactions, responsiveness, and validation across different browsers and devices.

---

## Manual Testing

Manual testing was carried out throughout development to verify that each feature worked as expected.

### Core Functionality Testing

| Feature | Test Action | Expected Result | Actual Result | Pass/Fail |
|-------|------------|----------------|---------------|-----------|
| Home Page | Load home page | Page loads correctly | Page loads correctly | Pass |
| Navigation | Click navigation links | Correct page loads | Correct page loads | Pass |
| User Registration | Submit valid registration form | Account created | Account created | Pass |
| User Registration | Submit empty form | Error messages displayed | Errors displayed | Pass |
| Login | Enter valid credentials | User logged in | User logged in | Pass |
| Login | Enter invalid credentials | Error message shown | Error shown | Pass |
| Logout | Click logout button | User logged out | User logged out | Pass |
| Create Item | Submit valid form | Item saved to database | Item saved | Pass |
| Update Item | Edit existing item | Changes saved | Changes saved | Pass |
| Delete Item | Delete item | Item removed | Item removed | Pass |
| Restricted Access | Access protected page while logged out | Redirected to login | Redirected correctly | Pass |

---

## Form Validation Testing

All forms were tested to ensure validation worked correctly:

- Required fields cannot be submitted empty
- Invalid email formats are rejected
- Password fields enforce minimum length
- Error messages display clearly to the user
- Forms submit successfully with valid input

---

## User Story Testing

User stories were tested to confirm that application functionality meets user expectations.

| User Story | Outcome |
|-----------|--------|
| As a user, I can register for an account | Users can successfully create an account |
| As a user, I can log in and out | Authentication works as expected |
| As a user, I can create content | Users can add new items |
| As a user, I can edit my content | Users can update their own items |
| As a user, I can delete my content | Users can delete their own items |
| As a user, I cannot edit others’ content | Access restrictions enforced |

---

## Responsiveness Testing

The application was tested for responsiveness using Chrome DevTools and real devices.

### Screen Sizes Tested
- Desktop (1920px and above)
- Tablet (iPad)
- Mobile (iPhone and Android)

The layout adapts correctly to all screen sizes with no horizontal scrolling issues.

---

## Browser Compatibility

The application was tested on the following browsers:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge

No major issues were identified across browsers.

---

## Automated Testing

Automated testing was not implemented for this project due to time constraints. However, comprehensive manual testing was carried out to ensure reliability and functionality across all core features.

---

## Bugs and Fixes

| Bug | Fix |
|----|----|
| Form submitted without required fields | Added required field validation |
| Navbar overflow on mobile devices | Updated CSS styling |
| Incorrect redirect after logout | Updated redirect logic |

All identified bugs were resolved during development.

---

## Validation Testing

The following validation tools were used:

- **HTML**: W3C Markup Validation Service
- **CSS**: W3C CSS Validator (Jigsaw)
- **Python**: PEP8 compliance checked using Flake8
- **JavaScript**: Checked for console errors using browser DevTools

No critical errors were found.

---

## Known Issues and Limitations

- Automated testing was not implemented
- Password reset functionality is not included
- Performance has not been optimised for large datasets

---

## Conclusion

All core functionality of the application was tested thoroughly through manual testing. The application performs as expected across supported devices and browsers, meeting the requirements of the Full Stack Development Level 5 assignment.
can