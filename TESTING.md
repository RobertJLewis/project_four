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
