# Project 4 – Food E-Commerce Store

## Introduction

**Project 4** is a full-stack e-commerce web application designed to deliver a seamless online shopping experience for food products. Built with user-centric design and modern development practices, the platform allows customers to browse, filter, and purchase food items intuitively—whether they're looking for everyday essentials or special treats.

The store is structured around four main browsing paths visible in the navigation bar:
- **Foods**: Filter by category — *Frozen*, *Whole Foods*, *Meat & Poultry*, or view *All Foods*
- **Drinks**: Choose between *Hot Beverages* and *Cold Drinks*, or see *All Drinks*
- **All Products**: Sort and explore everything by *Price*, *Rating*, *Category*, or view *All Products*
- **Special Offers**: Discover *New Arrivals*, *Deals*, *Clearance*, or browse *All Specials*

These filters are not just visual—they’re backed by dynamic frontend logic and a robust backend that supports real-time sorting and responsive data handling. Every interaction is designed to reduce friction and enhance usability, ensuring shoppers can find what they need quickly and confidently.

From strategy and wireframing to database design, authentication, testing, and deployment, **Project 4** demonstrates a complete implementation of full-stack development principles. This README serves as a comprehensive technical and design documentation of the entire project—covering goals, architecture, features, technologies used, and future enhancements.

Welcome to **Project 4**—where digital convenience meets everyday nourishment.

## Table of Contents

1. [Introduction](#introduction)
2. [Strategy Plane](#strategy-plane)
   - [Project Goals](#project-goals)
   - [Target Audience](#target-audience)
   - [Problem Statement](#problem-statement)
   - [Key Features](#key-features)
3. [Scope Plane](#scope-plane)
   - [Feature Planning](#feature-planning)
   - [Minimum Viable Product (MVP)](#minimum-viable-product-mvp)
4. [Structure Plane](#structure-plane)
   - [User Stories](#user-stories)
   - [User Flow Diagram](#user-flow-diagram)
5. [System Architecture](#system-architecture)
   - [Frontend Architecture](#frontend-architecture)
   - [Backend Architecture](#backend-architecture)
   - [API Design & Endpoints](#api-design--endpoints)
6. [Database Design](#database-design)
   - [Database Schema](#database-schema)
   - [Models & Relationships](#models--relationships)
   - [Data Validation & Integrity](#data-validation--integrity)
   - [Schema Diagram](#schema-diagram)
7. [Authentication & Authorization](#authentication--authorization)
   - [User Registration & Login](#user-registration--login)
   - [Permissions & Access Control](#permissions--access-control)
8. [Skeleton Plane (Wireframes)](#skeleton-plane-wireframes)
   - [Wireframes](#wireframes)
9. [Surface Plane (UI Design)](#surface-plane-ui-design)
   - [Colour Scheme](#colour-scheme)
   - [Typography](#typography)
   - [Imagery & Icons](#imagery--icons)
10. [Features](#features)
    - [User Dashboard](#user-dashboard)
    - [Search, Filter](#search-filter)
    - [Error Handling & Feedback](#error-handling--feedback)
11. [Frontend Implementation](#frontend-implementation)
    - [Templates & Components](#templates--components)
    - [Client-Side Logic](#client-side-logic)
12. [Backend Implementation](#backend-implementation)
    - [Views / Controllers](#views--controllers)
    - [Business Logic](#business-logic)
13. [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
    - [Validation Testing](#validation-testing)
14. [Security Considerations](#security-considerations)
    - [Data Protection](#data-protection)
    - [Environment Variables](#environment-variables)
15. [Accessibility](#accessibility)
16. [Deployment & Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Environment Configuration](#environment-configuration)
    - [Local Development Setup](#local-development-setup)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
17. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Libraries](#frameworks--libraries)
    - [Tools & Services](#tools--services)
18. [Future Enhancements](#future-enhancements)
19. [Credits & Acknowledgments](#credits--acknowledgments)

## Strategy Plane

### Project Goals

The primary goals of **Project 4** are to:
- Deliver a fully functional, responsive e-commerce platform focused exclusively on food and beverage products.
- Provide an intuitive user experience with clear navigation, dynamic filtering, and seamless product discovery.
- Implement secure user authentication, persistent shopping carts, and reliable data handling.
- Demonstrate mastery of full-stack development principles—including frontend interactivity, API integration, database modelling, and deployment best practices.
- Create a scalable foundation that can support future enhancements such as user reviews, inventory management, or email notifications.

### Target Audience

**Project 4** is designed for everyday consumers who value convenience, variety, and clarity when shopping for food online. Key user groups include:
- **Busy professionals** seeking quick, reliable access to groceries without visiting physical stores.
- **Students and young adults** looking for affordable, easy-to-prepare meals and snacks.
- **Health-conscious shoppers** interested in whole foods, fresh produce, and transparent categorisation.
- **Casual browsers** exploring deals, new arrivals, or seasonal offers.

The interface prioritises simplicity, fast loading, and mobile-friendly design to accommodate users across devices and technical comfort levels.

### Problem Statement

Many existing food e-commerce platforms suffer from cluttered interfaces, poor filtering logic, or overwhelming product lists that make it difficult for users to find what they need quickly. Smaller or concept-focused stores often lack robust technical foundations, leading to slow performance, inconsistent navigation, or limited functionality.

**Project 4** addresses these issues by offering a streamlined, category-driven shopping experience with smart filters (e.g., by price, rating, food type) and a clean information architecture—ensuring users can browse, compare, and select products with confidence and ease.

### Key Features

- **Category-Based Navigation**: Organised browsing via *Foods*, *Drinks*, *All Products*, and *Special Offers*.
- **Dynamic Filtering & Sorting**: Users can filter by subcategory (e.g., *Frozen*, *Meat & Poultry*) and sort by *Price* or *Rating*.
- **Responsive Product Listings**: Clean, consistent card-based layout with product images, names, prices, and ratings.
- **User Authentication**: Secure sign-up and login system to manage accounts and preferences.
- **Persistent Shopping Cart**: Items remain in the cart across sessions (via Django sessions or authenticated user data).
- **Structured Discovery**: Clear pathways to explore new arrivals, deals, and clearance items.
- **Mobile-First Design**: Fully responsive UI that works seamlessly on desktops, tablets, and smartphones.

## Scope Plane

### Feature Planning

To maintain focus and ensure timely delivery, features for **Project 4** were prioritised based on user needs, technical feasibility, and assignment requirements. The planned features are grouped as follows:

**Core Features (Included in MVP):**
- User authentication (registration, login, and session management via Django auth)
- Product browsing by main categories (*Foods*, *Drinks*, *All Products*, *Special Offers*) and subcategories (e.g., *Frozen*, *Meat & Poultry*, *Hot Beverages*)
- Dynamic filtering and sorting by price, rating, and category
- Responsive product listing and detail pages with images, descriptions, and pricing
- Shopping cart functionality (add, update quantity, remove items) with persistence across sessions
- Secure checkout flow powered by **Stripe**, including payment intent creation and success/cancel handling
- Order confirmation display post-payment

**Enhanced Features (Implemented or Planned):**
- Form validation for user registration and checkout inputs
- Error handling and user feedback (e.g., “Item added to cart”, “Payment successful”)
- Mobile-responsive design using hand-written CSS
- Basic order association for authenticated users

**Out-of-Scope (Not Implemented in This Version):**
- Admin dashboard for managing products (product data is seeded via fixtures or Django admin only)
- User reviews or ratings submission
- Email notifications (e.g., order confirmations via email)
- Inventory/stock-level tracking
- Password reset or advanced account management

This structured approach ensures a robust, secure, and user-friendly e-commerce experience while staying within project boundaries.

### Minimum Viable Product (MVP)

The **Minimum Viable Product (MVP)** for **Project 4** is a fully functional food e-commerce store built with **Django** and integrated with **Stripe** for real payment processing. It enables users to:
1. **Browse and filter** food and drink products through intuitive navigation (mirroring the live UI shown in the app).
2. **View product details** including name, image, price, and category.
3. **Add items to a shopping cart** that persists during the session and survives page reloads.
4. **Authenticate securely** to maintain cart state and access order-related features.
5. **Complete a real checkout flow** using **Stripe Elements**, where:
   - A payment intent is created server-side in Django
   - The user enters test card details via Stripe’s secure form
   - On success, the user sees an order confirmation; on cancellation, they’re redirected appropriately

Unlike basic demos, this MVP includes **end-to-end payment integration**, making it a production-ready foundation for a real food retail platform. All data is managed through a relational database (SQLite for development), and the application follows Django best practices for security, structure, and scalability.

## Structure Plane

### User Stories

User stories capture the core functionality of **Project 4** from the perspective of real users. Each story follows the format: *“As a [type of user], I want to [perform an action] so that [I achieve a goal].”*

- **As a guest shopper**, I want to see a clean landing page with clear navigation so I can quickly choose what to browse.
- **As a visitor**, I want to explore food and drink categories directly from the navbar (e.g., *Foods*, *Drinks*, *Special Offers*) so I don’t have to search blindly.
- **As a shopper**, I want to filter foods by type (*Frozen*, *Whole Foods*, *Meat & Poultry*) or drinks by temperature (*Hot Beverages*, *Cold Drinks*) so I can find relevant items fast.
- **As a returning user**, I want to log in so my cart and session data are preserved.
- **As a new user**, I want to register easily so I can proceed to checkout securely.
- **As a customer**, I want to add products to my cart and review them before paying.
- **As a buyer**, I want to complete payment using Stripe so my transaction is secure and reliable.
- **As a mobile user**, I want the navigation and filters to work smoothly on small screens so I can shop anywhere.

These stories ensured the interface remained focused, intuitive, and aligned with actual shopping behaviour.

### User Flow Diagram

The user journey in **Project 4** begins with a streamlined landing experience and progresses through intentional browsing—no overwhelming product grids on entry.

1. **Landing Page**  
   → User sees only a **hero image** and the **navigation bar**.  
   → No products are displayed yet—this encourages purposeful exploration via categories.

2. **Category Selection**  
   → User clicks a top-level nav item:  
     - **Foods** → reveals subcategories: *Frozen*, *Whole Foods*, *Meat & Poultry*, or *All Foods*  
     - **Drinks** → reveals: *Hot Beverages*, *Cold Drinks*, or *All Drinks*  
     - **All Products** → shows full catalog with sort options (*Price*, *Rating*, *Category*)  
     - **Special Offers** → displays *New Arrivals*, *Deals*, *Clearance*, or *All Specials*

3. **Product Listing View**  
   → After selecting a category/subcategory, the user sees a responsive grid of relevant products with images, names, prices, and ratings.

4. **Product Detail View**  
   → Clicking a product opens its detail page with full information.

5. **Cart Management**  
   → User adds items to cart; cart updates in real time (persisted via session or user account).

6. **Authentication (Before Checkout)**  
   → To proceed to payment, the user must be logged in (new users can register at this stage).

7. **Stripe Checkout**  
   → User is taken to a secure checkout page powered by **Stripe Elements**.  
   → Payment is processed in test mode during development.

8. **Post-Payment**  
   - **Success**: User sees a confirmation page with order summary.  
   - **Cancel/Fail**: User returns to cart with helpful feedback.

9. **Navigation Freedom**  
   → At any point, the user can return to the landing state or switch categories using the persistent navbar.

This flow prioritises **clarity over clutter**, guiding users from intention (“I want meat”) to action (“I’ve bought it”) without unnecessary steps.

## System Architecture

### Frontend Architecture

The frontend of **Project 4** is built using only core web technologies: **HTML5**, **CSS3**, and **vanilla JavaScript**—with no external UI libraries or frameworks.

- **HTML** provides semantic structure for all pages, including the minimal homepage (hero image + navigation bar) and product/category views.
- **CSS** handles all styling, including responsive layouts for mobile and desktop, with custom-designed product cards, buttons, and form elements.
- **JavaScript** is used sparingly and only where necessary:
  - Initialising **Stripe Elements** on the checkout page
  - Basic DOM updates (e.g., cart item count)
  - Form validation feedback
- No client-side routing or data fetching—most interactions trigger full page loads via standard HTML forms.

All content is rendered server-side by Django templates, ensuring fast initial load and straightforward maintenance.

### Backend Architecture

The backend is built with **Python** and the **Django** web framework, following the Model-View-Template (MVT) pattern.

- **Models** define the core data:
  - `Product`: name, description, price, category (e.g., "Foods"), subcategory (e.g., "Frozen"), image URL, rating
  - `User`: Django’s built-in authentication system
  - `Order`: stores completed purchases, linked to user and Stripe payment ID
- **Views** handle all logic using function-based views:
  - Render homepage, category pages, and product details
  - Process user registration/login via POST forms
  - Manage cart state using Django sessions (for guests) or user accounts
  - Initiate Stripe checkout and handle redirects
- **URLs** are clean and intuitive:
  - `/` → homepage  
  - `/foods/frozen/` → frozen food listings  
  - `/checkout/` → payment page
- **Security**:
  - CSRF protection on all forms
  - Passwords hashed automatically
  - Sensitive keys (e.g., Stripe, Gmail) stored in environment variables
- **Database**: SQLite for development, defined entirely through Django models.

### API Design & Endpoints

**Project 4 does not expose a public REST API** for products, users, or cart management. Instead, it uses **two external APIs** for specific functionality:

1. **Stripe API**  
   Used to process payments securely:
   - **`/create-checkout-session/`** (POST):  
     Server-side view that creates a Stripe PaymentIntent using the Stripe Python SDK. Returns a session ID or `client_secret` to the frontend.
   - **`/webhook/stripe/`** (POST):  
     Receives signed events from Stripe (e.g., `payment_intent.succeeded`). Verifies the signature and updates the order status accordingly.

2. **Gmail API (via Google OAuth)**  
   Used to send automated order confirmation emails:
   - After a successful payment, the backend uses the **Gmail API** (authenticated via a service account or OAuth 2.0) to send a formatted email to the customer.
   - This avoids relying on third-party email services and leverages Google’s secure email infrastructure.

> No internal JSON APIs were built for product listing or cart updates—all data is rendered directly in HTML templates. This keeps the architecture simple, secure, and focused on the core e-commerce flow.

## Database Design

### Database Schema

Project 4 uses a lightweight relational database managed by Django’s ORM with SQLite as the development backend. The schema is intentionally minimal and centres around three core tables: `auth_user` (Django’s built-in user model), `products_product`, and `orders_order`. All tables are defined through Django models and created via standard migrations, ensuring consistency between code and database structure without manual SQL.

### Models & Relationships

The `Product` model stores essential food and drink item details including name, description, price, category (e.g., "Foods" or "Drinks"), subcategory (such as "Frozen", "Meat & Poultry", or "Hot Beverages"), an image URL, and a numerical rating—fields that directly enable the navigation and filtering seen in the live interface. The `Order` model is created only after a successful Stripe payment and includes the unique `stripe_payment_intent_id`, total amount, currency, status, timestamp, and a foreign key linking to the authenticated user. Guest users are supported via session-based cart management, but orders are only finalised for logged-in users to ensure account association. There is no separate `Cart` or `OrderItem` model; instead, cart contents are held in Django sessions until checkout, at which point a single `Order` record is created, keeping the data model simple and focused.

### Data Validation & Integrity

Data integrity is enforced at the model level using Django’s built-in validation. Prices are restricted to non-negative values using `MinValueValidator`, ratings are constrained to a 1–5 range, and critical fields like `name` and `price` are marked as required. The Stripe webhook endpoint (`/webhook/stripe/`) further safeguards data consistency by verifying incoming event signatures with Stripe’s official library and checking whether a `payment_intent_id` has already been processed before creating a new order—this idempotency measure prevents duplicate orders in case of webhook retries. Session data for guest carts is securely signed and stored server-side by default, protecting against tampering.

### Schema Diagram

While a visual entity-relationship diagram was not generated programmatically, the logical structure is straightforward: the `User` table (from Django auth) has a one-to-many relationship with `Order`; each `Order` references one or more products indirectly via session data at checkout; and `Product` stands as a standalone reference table with no outgoing foreign keys. This clean, minimal design supports all required functionality—browsing, filtering, authentication, cart persistence, and secure payment—without unnecessary complexity.

## Authentication & Authorisation

### User Registration & Login

Project 4 implements user authentication using Django’s built-in `auth` system, providing secure and standards-compliant registration and login functionality. New users can create an account by submitting a registration form that collects a username, email, and password; passwords are automatically hashed using PBKDF2 before storage, ensuring sensitive credentials are never saved in plain text. The login process validates credentials against the database and establishes an authenticated session using Django’s session framework. All authentication views are served via server-rendered templates, with form submissions handled through standard POST requests. CSRF protection is enabled by default on all forms to prevent cross-site request forgery attacks, and error messages provide helpful—but not overly revealing—feedback in case of failed attempts.

### Permissions & Access Control

Access control in Project 4 follows a simple but effective role-based model: all visitors can browse products and add items to a session-based cart, but only authenticated users can proceed to checkout and complete a payment via Stripe. This ensures that every order is linked to a verified user account, enabling future features like order history or account management. No administrative or staff roles are implemented in this version, so there are no elevated permissions beyond standard user access. Sensitive views—such as the checkout page and order confirmation—are protected using Django’s `@login_required` decorator, which redirects unauthenticated users to the login page. Session data is managed securely using signed cookies, and user sessions expire after a period of inactivity, in line with Django’s default security settings. Overall, the approach balances usability with security, granting open access to browsing while reserving critical actions for verified users.

## Skeleton Plane (Wireframes)

### Wireframes

The wireframes for Project 4 were developed early in the design process to map out core user interactions and layout structure before any code was written. They reflect a mobile-first approach, prioritising clarity, usability, and alignment with the intended navigation flow. The homepage wireframe features only a full-width hero image and a persistent top navigation bar—intentionally minimal to encourage users to explore via category links rather than overwhelming them with content. Subsequent wireframes detail the product listing pages, showing a responsive grid of product cards displaying name, image, price, and rating, with filtering options accessible through the same navigation bar used on the homepage. The product detail page wireframe includes space for a larger image, description, price, and an “Add to Cart” button. The checkout flow is represented by a single dedicated screen that integrates Stripe Elements for secure card input, preceded by a cart summary view. All wireframes were sketched digitally using basic shapes and placeholders to focus on layout, hierarchy, and user flow—not visual design. These low-fidelity blueprints ensured that development remained focused on functionality and user experience, directly informing the final HTML structure and Django template organisation.

## Surface Plane (UI Design)

### Colour Scheme

The colour scheme for Project 4 is intentionally minimal and high-contrast, built primarily around **pure white (#FFFFFF) and black (#000000)** to create a clean, modern, and distraction-free shopping experience. This stark palette ensures maximum readability and puts full focus on product content and navigation. The only deliberate accent is a **vibrant yellow hero image** on the homepage, which serves as a bold visual anchor and emotional hook—evoking energy, freshness, and appetite without introducing additional UI colours. No other coloured elements are used in buttons, text, or backgrounds; interactive states (like hover effects) are indicated through subtle changes in opacity or underlines rather than colour shifts. This restrained approach reinforces simplicity, aligns with the project’s minimalist philosophy, and ensures strong accessibility through consistent contrast.

### Typography

Typography follows a no-frills, highly legible approach using system-default fonts to maintain performance and consistency across devices. The font stack is defined as `system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`, ensuring native rendering without external dependencies. All text appears in **black on a white background**, with clear hierarchy established through size and weight alone: headings use bold 24–28px type, product names appear at 18px bold, and body text (including prices and descriptions) is set at 16px regular weight. Line spacing and generous padding prevent visual crowding, especially on product listing pages. No custom fonts, italics, or decorative styles are used—typography exists purely to communicate information clearly and efficiently.

### Imagery & Icons

Imagery is used purposefully and sparingly. The **hero image—a bright yellow background with minimal or no additional graphics—dominates the homepage**, creating immediate visual impact while keeping the layout uncluttered. Product pages feature simple, consistent photography: each item is displayed against a plain white background with even lighting to ensure clarity and uniformity across the catalogue. No icons from external libraries are used; instead, functional cues are conveyed through text labels (e.g., “Add to Cart”) or basic Unicode symbols where appropriate. Buttons and navigation rely on typography and spacing—not iconography—to signal interactivity. This disciplined use of imagery keeps load times low and maintains the project’s focus on usability over decoration.

## Features

### User Dashboard

Project 4 does not include a traditional user dashboard with order history or account management. Instead, after successful authentication, users are able to proceed directly to checkout and receive immediate confirmation of their purchase on a dedicated success page. This streamlined approach prioritises the core shopping journey over secondary features, keeping the scope focused and development manageable. While future iterations could introduce a dashboard to display past orders or saved preferences, the current version ensures that user accounts serve their essential purpose: enabling secure, traceable transactions linked to a verified identity.

### Search, Filter

Navigation and filtering are central to the user experience in Project 4. Rather than a general search bar, the interface uses a **structured, category-driven filtering system** accessible through the persistent top navigation bar. Users can browse by main categories—**Foods**, **Drinks**, **All Products**, and **Special Offers**—each revealing relevant subcategories on click or hover (e.g., *Frozen*, *Meat & Poultry* under Foods; *Hot Beverages*, *Cold Drinks* under Drinks). On the “All Products” and “Special Offers” pages, users can further sort items by **price (low to high)** or **customer rating**. This intentional design reduces cognitive load by guiding users through logical pathways instead of overwhelming them with open-ended search, aligning with the minimalist ethos of the site. All filtering is handled server-side via Django views, ensuring fast, reliable results without client-side complexity.

### Error Handling & Feedback

Clear and helpful feedback is provided at key interaction points to enhance usability and prevent confusion. Form errors—such as mismatched passwords during registration or missing fields—are displayed inline with descriptive messages. During checkout, if a Stripe payment fails or is cancelled, the user is redirected back to the cart with a visible alert explaining what happened. Successful actions, like adding an item to the cart or completing a purchase, trigger immediate visual confirmation—either through page-level success messages or a dedicated order confirmation screen. The site also handles edge cases gracefully: invalid URLs return a standard 404 page, and unauthenticated users attempting to access checkout are redirected to the login page with a contextual prompt. These measures ensure that users always understand the system’s state and can recover from mistakes easily.

## Frontend Implementation

### Templates & Components

The frontend of Project 4 is built entirely using **Django’s templating system** with hand-written **HTML5 and CSS3**. There are no external UI libraries or component frameworks—every element is crafted from scratch to ensure full control and minimal overhead. A base template (`base.html`) defines the shared structure, including the persistent navigation bar and consistent page layout, which all other pages extend using Django’s `{% extends %}` and `{% block %}` syntax. The homepage template renders only a full-width hero image and the navigation bar, reflecting the intentional minimalism of the landing experience. Product listing and detail pages dynamically inject content into this structure using context data passed from Django views, ensuring that category filters, product cards, and pricing are rendered server-side with no client-side data fetching. Each product card follows a uniform design—image, name, price, and rating—styled consistently through a single CSS file. This template-driven approach keeps the frontend simple, fast-loading, and tightly integrated with the backend logic.

### Client-Side Logic

Client-side interactivity is limited to essential enhancements using **vanilla JavaScript**, with no dependencies or build tools. A small script is included only on the checkout page to initialise **Stripe Elements**, securely loading Stripe’s JavaScript library from their official CDN and mounting the card input field. Elsewhere, JavaScript is used sparingly: a lightweight function toggles the mobile menu on smaller screens, and another updates the cart item count in the navigation bar when items are added (via DOM manipulation after form submission). Form validation for registration and login is handled primarily by Django server-side, but basic front-end checks (e.g., password length, required fields) provide immediate feedback without full page reloads. No AJAX calls are used for product browsing or cart updates—all interactions rely on standard HTML form submissions and full-page rendering, prioritising simplicity and reliability over dynamic behaviour. This restrained use of client-side logic ensures the site remains accessible, maintainable, and performant across all devices.

## Backend Implementation

### Views / Controllers

The backend of Project 4 is implemented using **Django’s function-based views**, which handle all routing and rendering logic in a clear and maintainable way. Each URL path maps directly to a view that processes the request, retrieves or manipulates data, and returns an appropriate HTTP response. The homepage view renders only the hero image and navigation bar, while category-specific views—such as `foods_view`, `drinks_view`, or `specials_view`—filter products by category and subcategory using simple ORM queries (e.g., `Product.objects.filter(category='Foods', subcategory='Frozen')`). The product detail view fetches a single item by ID, and the checkout view handles both cart display and Stripe session creation. Authentication views leverage Django’s built-in `LoginView` and custom registration logic, ensuring secure user handling without reinventing core functionality. All views pass contextual data to templates using standard Python dictionaries, keeping the separation between logic and presentation clean and readable.

### Business Logic

Core business logic is embedded within views and model methods, following Django best practices for simplicity and testability. Cart management is handled through **Django sessions**: when a user adds an item, the product ID and quantity are stored in the session dictionary, and this data persists across page loads until checkout. During checkout, the system validates that the cart is not empty and that the user is authenticated before proceeding. The Stripe integration is managed entirely server-side: the `/create-checkout-session/` view uses the Stripe Python SDK to create a `PaymentIntent` with the correct amount and currency, then returns the client secret to the frontend for confirmation. After payment, the Stripe webhook endpoint verifies the event signature and, upon receiving a `payment_intent.succeeded` event, creates a permanent `Order` record linked to the user and payment intent ID. This ensures that orders are only recorded for genuine, verified transactions. No complex workflows or external services are used—business rules remain focused, auditable, and tightly coupled to the actual user journey.

## Testing

A comprehensive testing strategy was applied throughout the development of Project 4 to ensure reliability, usability, and correctness. Full details of all test activities—including manual test cases, automated unit/integration tests, and front-end validation checks—are documented in a dedicated file:

➡️ **[View full testing report](./testing.md)**

This includes:
- **Manual Testing**: Step-by-step user journey validation (e.g., browsing categories, adding to cart, completing Stripe checkout)
- **Automated Testing**: Django unit tests for models, views, and Stripe webhook logic
- **Validation Testing**: HTML/CSS validation, form error handling, and accessibility checks

The `testing.md` file serves as the complete audit trail for quality assurance in this project.

## Security Considerations

### Data Protection

Project 4 follows core web security best practices to protect user data and maintain system integrity. All user passwords are automatically hashed using Django’s default PBKDF2 algorithm—never stored in plain text. Sensitive operations, such as login and registration, are protected against cross-site request forgery (CSRF) using Django’s built-in middleware, which validates tokens on all POST requests. Session data—including guest cart contents—is stored securely using signed cookies, preventing client-side tampering. The Stripe integration is implemented in a PCI-compliant manner: payment details are entered directly into Stripe Elements (loaded from Stripe’s official CDN), meaning **no card data ever touches the Django application or database**. Orders are only created after verifying Stripe webhook signatures using the `stripe.Webhook.construct_event()` method, ensuring that payment events originate from Stripe and not a malicious source. Additionally, all user-facing forms include basic validation to prevent malformed or excessive input, reducing the risk of injection attacks.

### Environment Variables

All sensitive configuration data is kept out of the codebase and managed through environment variables. This includes the Django `SECRET_KEY`, `DEBUG` setting, database credentials (if used in production), Stripe API keys (`STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY`), and Gmail API credentials (such as OAuth client ID or service account details). These values are loaded at runtime using Python’s `os.getenv()` or a lightweight package like `python-decouple` (if used), ensuring that secrets are never committed to version control. A `.env.example` file is included in the repository to document required variables without exposing actual values. This approach aligns with the Twelve-Factor App methodology and significantly reduces the risk of accidental credential leakage during development or deployment.

## Accessibility

Project 4 prioritises basic web accessibility to ensure the site is usable by as many people as possible. The markup follows semantic HTML5 principles: headings are used in a logical hierarchy (`<h1>` for page titles, `<h2>` for sections), navigation is wrapped in a `<nav>` element, and product listings are structured within `<main>` and `<section>` tags. All interactive elements—such as links and buttons—are keyboard-navigable and display visible focus states using default browser outlines or custom CSS that maintains sufficient contrast. Form labels are explicitly associated with their inputs using the `for` and `id` attributes, ensuring screen readers can correctly announce field purposes. Images include descriptive `alt` attributes (e.g., “Organic bananas, bunch of six”); decorative images like the yellow hero background use empty `alt=""` to be ignored by assistive technology. Colour contrast between text and background meets WCAG AA standards, leveraging the high-contrast black-on-white palette for optimal readability. While advanced ARIA roles or dynamic announcements (e.g., for cart updates) were not implemented due to the project’s scope, the foundation remains solid, semantic, and compatible with standard screen readers and assistive tools.

## Deployment & Local Development

### Deployment

Project 4 is designed to be deployable to any platform that supports Python and Django applications, such as **Render**, **Railway**, or **Heroku**. The current setup uses **SQLite** for development, but the settings are structured to easily switch to **PostgreSQL** in production by updating the `DATABASES` configuration. Static files (CSS, images) are served via Django’s built-in static file handling during development and can be configured for CDN or cloud storage in production. Environment variables are used for all sensitive settings, ensuring secrets like `SECRET_KEY` and `STRIPE_SECRET_KEY` are never exposed in code. The application includes a `requirements.txt` file listing all Python dependencies, enabling one-command installation in any environment. While not yet deployed publicly, the project follows deployment-ready conventions, including proper `.gitignore` rules and separation of settings for different environments.

### Environment Configuration

All sensitive and environment-specific values are managed through **environment variables**, not hardcoded in source files. These include `SECRET_KEY`, `DEBUG`, `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, and Gmail API credentials. A `.env.example` file is included in the repository to document required variables, while the actual `.env` file is excluded from version control via `.gitignore`. At runtime, these values are loaded using Python’s `os.getenv()` (or a minimal loader like `python-decouple` if used). The `DEBUG` setting is explicitly set to `False` in production-like configurations to prevent leakage of internal system details. This approach ensures the same codebase can run securely across local, staging, and production environments with only configuration changes.

### Local Development Setup

To run Project 4 locally, you’ll need Python 3.10+ and pip installed on your machine. The project uses a virtual environment to isolate dependencies, ensuring consistent behaviour across systems.

#### How to Fork

To create your own copy of the repository, go to the project’s GitHub page and click the **Fork** button in the top-right corner. This will create a personal copy under your GitHub account, allowing you to make changes without affecting the original.


#### How to Clone

Once forked (or if cloning the original), open your terminal and run:  
-bash
git clone https://github.com/your-username/project_four_2025.git
cd project-4


## Technologies Used

### Languages

Project 4 is built using core web languages: **Python** for all backend logic and server-side processing, **HTML5** for semantic document structure, **CSS3** for styling and responsive layout, and **vanilla JavaScript** for minimal client-side interactivity. No transpiled or alternative languages—such as TypeScript, Sass, or JSX—were used, ensuring the codebase remains transparent, accessible, and straightforward to debug. Python drives Django’s models, views, and URL routing, while HTML, CSS, and JavaScript work in harmony to deliver a fast, semantic, and mobile-friendly user interface.

### Frameworks & Libraries

The project relies exclusively on **Django 5.x** as the backend framework, leveraging its built-in features for authentication, ORM, templating, and security. Payment functionality is implemented using the official **Stripe Python SDK** to create and verify payment intents server-side, while **Stripe.js (v3)** is loaded securely from Stripe’s CDN on the checkout page to handle card input without exposing sensitive data. No frontend frameworks (e.g., React or Vue) or UI libraries (e.g., Bootstrap or Tailwind CSS) are used—styling is hand-coded in plain CSS to maintain full control and minimise dependencies. Similarly, only essential Python packages are included (notably `stripe` and optionally `python-decouple` for environment variable management), keeping the project lightweight and focused.

### Tools & Services

Development was carried out in **Visual Studio Code**, with Git integration for version control via **GitHub**. The application uses **SQLite** as the local database during development, with schema changes managed entirely through Django migrations. For external services, **Stripe** handles all payment processing in test mode, and the **Gmail API** (authenticated via Google Cloud OAuth) is used to send order confirmation emails. Sensitive configuration is stored in a `.env` file (excluded from version control), and project dependencies are clearly listed in `requirements.txt`. The workflow remains deliberately simple—no bundlers, linters, or CI/CD pipelines were implemented—to prioritise clarity and core full-stack learning outcomes.

## Future Enhancements

While Project 4 delivers a complete and functional food e-commerce experience, several enhancements could be introduced in future iterations to improve usability, scalability, and user engagement. A dedicated **user dashboard** would allow customers to view order history, save favourite items, and manage account details. Adding a **global search bar** would enable keyword-based discovery across all product categories. The cart system could be enhanced to support **persistent storage for guest users** using browser local storage or a lightweight database-backed session model, and **real-time inventory tracking** could prevent overselling of popular items. Additional features might include **user-submitted reviews and ratings**, **automated email notifications** (via the Gmail API) for order confirmations and shipping updates, and a custom **admin interface** for non-technical team members to manage products. On the technical side, migrating to **PostgreSQL** for production, expanding **automated test coverage**, and introducing a basic **CI/CD pipeline** would further strengthen reliability and maintainability—all while preserving the project’s clean, minimalist architecture.

## Credits & Acknowledgments

Project 4 was developed independently as part of a full-stack web development assignment. I would like to acknowledge the open-source communities behind **Django**, **Python**, and **Stripe** for providing robust, well-documented, and secure tools that made this project possible. Special thanks to the creators of **Visual Studio Code** for an excellent, accessible development environment, and to **Google** for the clear documentation and reliable infrastructure of the **Gmail API** and **OAuth 2.0** system. All product images used in the application are either original placeholders or sourced from royalty-free repositories for educational purposes only. This project reflects my own implementation, problem-solving, and understanding of full-stack principles—built with care, attention to detail, and a commitment to both user experience and technical integrity.