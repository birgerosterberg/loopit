# Manual Testing Documentation for LoopIt

## Test Scenarios

### Test Scenario 1: Navbar Visibility and Functionality

#### User Roles:

- Non-logged-in User
- Logged-in User
- Superuser

#### Test Description:

Test the Navbar to ensure that it displays the correct options based on the user's role and that each option redirects to the appropriate page.

#### Test Steps and Results:

| User Type          | Test Steps                           | Expected Results                                         | Actual Results       | Status                                  |
| ------------------ | ------------------------------------ | -------------------------------------------------------- | -------------------- | --------------------------------------- |
| Non-logged-in User | 1. View the page without logging in. | Only "Home", "Login", and "Register" are visible.        | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Click "Home".                     | Should redirect to the homepage.                         | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 3. Click "Login".                    | Should redirect to the login page.                       | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 4. Click "Register".                 | Should redirect to the registration page.                | Behaved as expected. | <span style="color:green">Passed</span> |
| Logged-in User     | 1. Log in as a regular user.         | "Home", "Logout", and "My Profile" are visible.          | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Click "Home".                     | Should redirect to the homepage.                         | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 3. Click "Logout".                   | Should log out and redirect to the homepage.             | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 4. Click "My Profile".               | Should redirect to the user's profile page.              | Behaved as expected. | <span style="color:green">Passed</span> |
| Superuser          | 1. Log in as a Superuser.            | "Home", "Logout", "My Profile", and "Admin" are visible. | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Click "Home".                     | Should redirect to the homepage.                         | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 3. Click "Logout".                   | Should log out and redirect to the homepage.             | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 4. Click "My Profile".               | Should redirect to the user's profile page.              | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 5. Click "Admin".                    | Should redirect to the admin dashboard.                  | Behaved as expected. | <span style="color:green">Passed</span> |

---

### Test Scenario 2: "Create Post" Button Visibility

#### User Roles:

- Non-logged-in User
- Logged-in User
- Superuser

#### Test Description:

Test to ensure that the "Create Post" button is visible only for Logged-in Users and Superusers, and not visible for Non-logged-in Users.

#### Test Steps and Results:

| User Type          | Test Steps                           | Expected Results                            | Actual Results       | Status                                  |
| ------------------ | ------------------------------------ | ------------------------------------------- | -------------------- | --------------------------------------- |
| Non-logged-in User | 1. View the page without logging in. | "Create Post" button should not be visible. | Behaved as expected. | <span style="color:green">Passed</span> |
| Logged-in User     | 1. Log in as a regular user.         | "Create Post" button should be visible.     | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Click "Create Post".              | Should redirect to the "Create Post" page.  | Behaved as expected. | <span style="color:green">Passed</span> |
| Superuser          | 1. Log in as a Superuser.            | "Create Post" button should be visible.     | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Click "Create Post".              | Should redirect to the "Create Post" page.  | Behaved as expected. | <span style="color:green">Passed</span> |

---

### Test Scenario 3: "Create Post" Page Accessibility and Functionality

#### User Roles:

- Non-logged-in User
- Logged-in User
- Superuser

#### Test Description:

To test if the "Create Post" page is only accessible by Logged-in Users and Superusers. Also, to ensure that all fields (Title, Content, Category) are mandatory for creating a post.

#### Test Steps and Results:

| User Type          | Test Steps                                               | Expected Results                                      | Actual Results       | Status                                  |
| ------------------ | -------------------------------------------------------- | ----------------------------------------------------- | -------------------- | --------------------------------------- |
| Non-logged-in User | 1. Attempt to navigate to `/url/create_post/`.           | Should be redirected to the login page.               | Behaved as expected. | <span style="color:green">Passed</span> |
| Logged-in User     | 1. Log in as a regular user.                             | Should be able to navigate to the "Create Post" page. | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Fill in only Title, leave Content and Category blank. | Should not be able to create the post.                | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 3. Fill in only Content, leave Title and Category blank. | Should not be able to create the post.                | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 4. Fill in only Category, leave Title and Content blank. | Should not be able to create the post.                | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 5. Fill in all fields (Title, Content, Category).        | Should be able to create a post.                      | Behaved as expected. | <span style="color:green">Passed</span> |
| Superuser          | 1. Log in as a Superuser.                                | Should be able to navigate to the "Create Post" page. | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Fill in only Title, leave Content and Category blank. | Should not be able to create the post.                | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 3. Fill in only Content, leave Title and Category blank. | Should not be able to create the post.                | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 4. Fill in only Category, leave Title and Content blank. | Should not be able to create the post.                | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 5. Fill in all fields (Title, Content, Category).        | Should be able to create a post.                      | Behaved as expected. | <span style="color:green">Passed</span> |

---

### Test Scenario 4: Category Filter Functionality

#### User Roles:

- All Users

#### Test Description:

To test if selecting a category filters the posts accordingly and highlights the selected category. The available categories are All, General, Hardware, Software, Promotion, Inspiration.

#### Test Steps and Results:

| User Type | Test Steps                                       | Expected Results                                                                                  | Actual Results       | Status                                  |
| --------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------------- |
| All Users | 1. Select "All" from the categories row.         | All posts should be displayed. "All" should be marked as active.                                  | Behaved as expected. | <span style="color:green">Passed</span> |
|           | 2. Select "General" from the categories row.     | Only posts tagged as "General" should be displayed. "General" should be marked as active.         | Behaved as expected. | <span style="color:green">Passed</span> |
|           | 3. Select "Hardware" from the categories row.    | Only posts tagged as "Hardware" should be displayed. "Hardware" should be marked as active.       | Behaved as expected. | <span style="color:green">Passed</span> |
|           | 4. Select "Software" from the categories row.    | Only posts tagged as "Software" should be displayed. "Software" should be marked as active.       | Behaved as expected. | <span style="color:green">Passed</span> |
|           | 5. Select "Promotion" from the categories row.   | Only posts tagged as "Promotion" should be displayed. "Promotion" should be marked as active.     | Behaved as expected. | <span style="color:green">Passed</span> |
|           | 6. Select "Inspiration" from the categories row. | Only posts tagged as "Inspiration" should be displayed. "Inspiration" should be marked as active. | Behaved as expected. | <span style="color:green">Passed</span> |
