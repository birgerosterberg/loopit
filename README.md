# Loopit - A Community for Loopers

## Loopit is an online community designed for enthusiasts of a special unique art of music creation, where looping machines like the famous BOSS RC505 are often used. This Django-based web application provides a platform for musicians to collaborate, share tips and tutorials, and discuss their love for this unique art form.

## Agile Planning and Development Process

The development of Loopit followed an Agile methodology, utilizing a Kanban board hosted on GitHub to manage tasks and workflows. This approach made it easier to focus on immediate tasks while also keeping an eye on the broader project goals and progress.

### Kanban Board

The board was divided into three primary columns:

- **Todo**: Tasks that are planned but not yet in progress.
- **In Progress**: Tasks currently being worked on.
- **Done**: Tasks that have been completed.

Each task was created as an issue and then categorized into Epics and User Stories for better organization and focus.

### Epics and User Stories

Prior to starting development, Epics and User Stories were created to define the scope and goals of the project. This made it easier to break down the project into smaller, manageable chunks and helped in tracking progress effectively.

- **Epics**: Large areas of work that contain multiple tasks.
- **User Stories**: Smaller tasks that contribute to the completion of an Epic.

This Agile planning setup contributed significantly to the efficient and focused development of Loopit.

### Base Setup:

**Epic 1: Base Setup** \
**Description: The base setup epic is for all stories needed for the base set up of the application. Without the base setup, the app would not be possible, so it was the first epic to be delivered as all other features depend on the completion of the base setup.**

User Stories: \
As a developer, I need to create the base.html page and structure so that other pages can reuse the layout \
As a developer, I need to create static resources so that images, css and javascript work on the website \
As a developer, I need to set up the project so that it is ready for implementing the core features \
As a developer, I need to create the footer with social media links and contact information \
As a developer, I need to create the navbar so that users can navigate the website from any device

### User Management:

**Epic 2: User Registration and Authentication** \
**Description: Develop user registration and authentication functionalities to allow users to create accounts, log in, log out, and reset passwords.**

User Stories: \
As a new user, I want to create an account so that I can start using the LoopIt. \
As a registered user, I want to be able to log in and log out of my account. \
X As a registered user, I want to reset my password if I forget it.

**Epic 3: User Profile and Settings** \
**Description: Implement user profiles where users can view their activity, customize display names, and upload profile pictures.**

User Stories: \
X As a user, I want to have a profile page where I can see my posts and likes. \
As a user, I want to customize my display name and profile picture.

### Content Management:

**Epic 4: Post Creation and Management** \
**Description: Build the functionality to manage posts, including creating, editing, and deleting posts, as well as viewing a list of posts.**

User Stories: \
As a user, I want to view a list of posts shared by other loop artists. \
As a user, I want to create a new post to share my own content, including the ability to add a YouTube video or post an image. \
As a user, I want to edit my own posts if I need to update the content. \
As a user, I want to delete my own posts if I decide to remove them.

**Epic 5: Interaction (Liking, Commenting, Rating and Reporting)** \
**Description: Enable users to interact with posts by liking, commenting, reporting and rating them.**

User Stories: \
X As a user, I want to like posts that I find interesting to show appreciation for the content. \
As a user, I want to comment on posts to engage with the community and share my thoughts. \
X As a user, I want to rate posts using a heart-based system to express my opinion about the quality of the content. \
As a user, I want to report a post if I find it inappropriate, offensive, or violating the community guidelines. \
As a user, I want to report a comment that I believe is inappropriate or offensive.

### Deployment and Documentation:

**Epic 6: Deployment and Hosting** \
**Description: Prepare your application for deployment and choose a hosting platform to make it accessible online.**

User Stories: \
As a developer, I want to configure production settings for my Django application. \
As a developer, I want to set up a production-ready database (e.g., PostgreSQL) for my application. \
As a developer, I want to deploy my Django application to Heroku. \
As a user, I want to access the LoopIt online through a secure URL. \
As a user, I want the deployed application to handle traffic efficiently and reliably.

**Epic 7: Documentation** \
**Description: Create comprehensive documentation to guide users and other developers in using and contributing to your project.**

User Stories: \
As a developer, I want to provide a README file with setup instructions for local development. \
As a developer, I want to document the application's features, including how to create an account, post content, and interact with posts. \
As a developer, I want to explain the structure of the project, including its models, views, and templates. \
As a developer, I want to document any third-party libraries used in the project.

## Site Goals

1. **Create a Safe Space for Creativity**: To provide an environment where loopers can share their work without fear of harsh judgement or copyright infringement.
2. **Foster Collaboration**: To facilitate connections between musicians for potential collaborations and creative exploration.
3. **Knowledge Sharing**: To become a repository of tutorials, guides, and other educational resources related to loop-based music.
4. **Expand the Community**: To introduce more people to the joy and creative possibilities of loop-based music.
5. **Event Promotion**: To be the go-to platform for discovering and promoting events related to this genre of music.

## Project Scope and Technical Features

### Scope

The scope of Loopit was carefully defined to create a focused and user-friendly platform. Key elements include:

- Providing a community space specifically geared towards loop-based music enthusiasts.
- Offering functionalities that support collaboration, sharing, and learning.
- Ensuring a secure and safe environment for all users to freely express themselves and share content.

### Technical Features

#### Responsive Design

Loopit was built with a responsive design to ensure an optimal user experience across a variety of devices, including desktops, tablets, and smartphones.

#### CRUD on Posts

The platform allows for full CRUD (Create, Read, Update, Delete) operations on user-generated posts. This enables users to freely share their insights, ask questions, and interact with the community.

#### Simple Easy Design

Ease of use was a primary consideration during the design phase. Loopit features a clean, intuitive interface that lets users navigate the site with minimal effort.

Credits: \
https://www.pngegg.com/en/png-zepmn - Infinity symbol default.jpg
