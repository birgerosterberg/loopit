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

---

### Test Scenario 5: Viewing Individual Post Pages

#### User Roles:

- Author (User who owns the post)
- Logged-in User (not the author)
- Non-logged-in User

#### Test Description:

To test the different viewing options and buttons available on individual post pages based on the user role.

#### Test Steps and Results:

| User Type          | Test Steps                                                  | Expected Results                                                                                                                            | Actual Results       | Status                                  |
| ------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------------- |
| Author             | 1. Log in and navigate to a post you authored.              | Should see the post along with Edit and Delete options. Should also see the "Report" button on the post, and the "Create a Comment" fields. | Behaved as expected. | <span style="color:green">Passed</span> |
|                    |                                                             |                                                                                                                                             |                      |                                         |
| Logged-in User     | 1. Log in as a different user (not the author of the post). | Should see the post, the "Report" button on the post, and the "Create a Comment" fields.                                                    | Behaved as expected. | <span style="color:green">Passed</span> |
|                    |                                                             |                                                                                                                                             |                      |                                         |
| Non-logged-in User | 1. View the post without logging in.                        | Should see the post and the comments made on it. No "Report" button or "Create a Comment" fields visible.                                   | Behaved as expected. | <span style="color:green">Passed</span> |

---

### Test Scenario 6: Testing the "Report" Functionality

#### User Roles:

- Logged-in User
- Non-logged-in User

#### Test Description:

To test if the "Report" function can be used by a Logged-in User to report a post or a comment. Also to test if a Non-logged-in User can access the URL for reporting.

#### Test Steps and Results:

| User Type          | Test Steps                                                                           | Expected Results                                       | Actual Results       | Status                                  |
| ------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------ | -------------------- | --------------------------------------- |
| Logged-in User     | 1. Log in and navigate to a post or comment.                                         | Should see the "Report" button on the post or comment. | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Click the "Report" button on the post or comment.                                 | Should be able to report the post or comment.          | Behaved as expected. | <span style="color:green">Passed</span> |
| Non-logged-in User | 1. Try to directly access the URL for the "Report" functionality without logging in. | Should be redirected to the login page.                | Behaved as expected. | <span style="color:green">Passed</span> |

---

### Test Scenario 7: Admin/Superuser Viewing Reports

#### User Roles:

- Admin / Superuser

#### Test Description:

To test if the Admin or Superuser can view reports made on posts or comments after they have been reported.

#### Test Steps and Results:

| User Type       | Test Steps                                                                            | Expected Results                                               | Actual Results       | Status                                  |
| --------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------- | --------------------------------------- |
| Admin/Superuser | 1. Log in as Admin or Superuser and navigate to the section where reports are listed. | Should be able to see the list of reported posts and comments. | Behaved as expected. | <span style="color:green">Passed</span> |

---

### Test Scenario 8: Edit and Delete Posts

#### User Roles:

- Author (User who owns the post)
- Non-logged-in User
- Non-author Logged-in User

#### Test Description:

To test the edit and delete functionalities of posts, making sure they are restricted based on user roles and function as designed.

#### Test Steps and Results:

| User Type                 | Test Steps                                                                               | Expected Results                                                                                                  | Actual Results       | Status                                  |
| ------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------------- |
| Author                    | 1. Log in and navigate to a post you authored.                                           | Should see the "Edit" and "Delete" options.                                                                       | Behaved as expected. | <span style="color:green">Passed</span> |
|                           | 2. Click on the "Edit" button and make changes.                                          | Should be directed to the Edit page, and upon making changes and submitting, redirected back to the updated post. | Behaved as expected. | <span style="color:green">Passed</span> |
|                           | 3. Click on the "Delete" button.                                                         | Should be directed to a confirmation page asking to confirm the delete action.                                    | Behaved as expected. | <span style="color:green">Passed</span> |
|                           | 4. Confirm the delete action.                                                            | Should be redirected to the front page with a "Post has been deleted" message.                                    | Behaved as expected. | <span style="color:green">Passed</span> |
| Non-logged-in User        | 1. Navigate to a post without logging in.                                                | Should not see "Edit" and "Delete" options.                                                                       | Behaved as expected. | <span style="color:green">Passed</span> |
|                           | 2. Try to directly access the Edit/Delete URL for that specific post without logging in. | Should be redirected to the login page.                                                                           | Behaved as expected. | <span style="color:green">Passed</span> |
| Non-author Logged-in User | 1. Log in and navigate to a post you did not author.                                     | Should not see "Edit" and "Delete" options.                                                                       | Behaved as expected. | <span style="color:green">Passed</span> |
|                           | 2. Try to directly access the Edit/Delete URL for that specific post while logged in.    | Should not be able to edit or delete the post. Should be redirected or see an unauthorized message.               | Behaved as expected. | <span style="color:green">Passed</span> |

---

### Test Scenario 9: Create a Comment

#### User Roles:

- Logged-in User
- Non-logged-in User

#### Test Description:

To test the functionality of creating a comment on a post as a logged-in user.

#### Test Steps and Results:

| User Type          | Test Steps                                                  | Expected Results                                                                                                              | Actual Results       | Status                                  |
| ------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------------- |
| Logged-in User     | 1. Log in and navigate to a post.                           | Should see a comment field with a "Submit" button.                                                                            | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Write something in the comment field and click "Submit". | Comment should be created, username should be displayed along with time and date. Comment count on post should increase by 1. | Behaved as expected. | <span style="color:green">Passed</span> |
| Non-logged-in User | 1. Navigate to a post without logging in.                   | Should not see the comment field or "Submit" button.                                                                          | Behaved as expected. | <span style="color:green">Passed</span> |

---

### Test Scenario 10: Account Creation (Registration)

#### User Roles:

- Non-logged-in User

#### Test Description:

To test the functionality of account creation via the Signup page.

#### Test Steps and Results:

| User Type          | Test Steps                                                                                                                                        | Expected Results                                                                                                   | Actual Results       | Status                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------- | --------------------------------------- |
| Non-logged-in User | 1. Navigate to the Signup page by clicking the "Register" button.                                                                                 | Should be taken to the Signup page, with fields for username, optional email, password, and password confirmation. | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 2. Enter an improperly formatted email (e.g., "wrongemail.com") and click the "Sign Up" button.                                                   | Should see an error message indicating that the email format is incorrect.                                         | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 3. Enter a non-unique username and click the "Sign Up" button.                                                                                    | Should see an error message stating that the username needs to be unique.                                          | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 4. Enter a weak password and click the "Sign Up" button.                                                                                          | Should see an error message about the password not being strong enough.                                            | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 5. Enter differing passwords in the "Password" and "Repeat Password" fields, then click the "Sign Up" button.                                     | Should see an error message stating that the passwords do not match.                                               | Behaved as expected. | <span style="color:green">Passed</span> |
|                    | 6. Fill in all fields correctly with a properly formatted email, unique username, and matching strong passwords, then click the "Sign Up" button. | Should successfully create the account and be redirected to the frontpage.                                         | Behaved as expected. | <span style="color:green">Passed</span> |
