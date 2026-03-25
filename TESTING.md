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




### W3C CSS Validation

The **W3C CSS Validator** was used to validate all custom CSS files within **Project 4 – Food E-Commerce Store**. Each stylesheet was tested individually to ensure compliance with **CSS3 standards**, proper syntax, and cross-browser compatibility.

| File Tested                              | Result | Evidence |
|------------------------------------------|--------|----------|
| `static/css/base.css`                    | Pass   | base.css validation |
| `checkout/static/checkout/css/checkout.css` | Pass   | checkout.css validation |
| `profiles/static/profiles/css/profile.css` | Pass   | profile.css validation |

> All stylesheets passed validation with no critical errors, confirming clean, standards-compliant CSS and consistent rendering across modern browsers.




### JavaScript Validation

All custom JavaScript files were validated using **JSHint** to ensure proper syntax, code quality, and adherence to modern best practices.

| File Tested                                      | Result | Evidence             | Notes |
|--------------------------------------------------|--------|----------------------|-------|
| `checkout/static/checkout/js/stripe-elements.js` | Pass   | stripe-elements.js   | Initial warnings related to ES6 template literals were resolved by updating the JSHint configuration to ES8 using `/* jshint esversion: 8 */`. |

> All JavaScript files passed validation after minor configuration adjustments, ensuring clean, maintainable, and standards-compliant client-side code.



### Python Validation

All Python code was validated using the **Code Institute Python Linter**, ensuring compliance with **PEP8 (Python Enhancement Proposal 8)** — the official Python style guide. This guarantees consistent formatting, readability, and maintainable code across the entire project.

