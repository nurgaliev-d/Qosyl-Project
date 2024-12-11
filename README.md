# Qosyl app

Purpose of this Django project is to create a social platform where users can join rooms based on topics of interest, communicate through messages, and engage with each other through friendships and comments. Users can send and receive friend requests, participate in discussions, and track activity across rooms.

****

****


# Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [App Source](#app-source)
4. [Basic information about App](#app-description)
5. [Project preview](#project-preview)
6. [Project members](#project-members)
7. [Project Technical Topics that Containing Now](#used-topics-at-this-time)

# Prerequisites
Before you can run this project, make sure your system meets the following requirements:

1. **Python**:
   - Version: 3.8 or higher
   - [Download Python](https://www.python.org/downloads/)
2. **Pip**:
   - Installed alongside Python for managing Python packages.
3. **Virtual Environment (Optional but recommended)**:
   - Install `venv` or any virtual environment manager like `virtualenv`.
4. **Git**:
   - Version control system to clone the repository.
   - [Download Git](https://git-scm.com/)
5. **SQLite**:
   - Pre-installed with Python. Used as the default database for development.

---
# Installation
Follow the steps below to set up and run the Qosyl Project locally.

---

## Installation Steps

### 1. Clone the Repository
Clone the repository and navigate into the project folder:
`git clone https://github.com/nurgaliev-d/Qosyl-Project.git
cd Qosyl-Project`

### 2. Set Up a Virtual Environment
Create and activate a virtual environment:
`python -m venv venv`
Activate the virtual environment:

Linux/macOS:
`source venv/bin/activate`
Windows:
`venv\Scripts\activate`

### 3. Install Dependencies
Install the required Python packages:
`pip install -r requirements.txt`



### Database Setup
1. Apply Migrations
Set up the database schema:
`python manage.py migrate`

2. Create a Superuser
Create an admin user to access the Django admin interface:
`python manage.py createsuperuser`

### Running the Project
Start the Django development server:
`python manage.py runserver`

Access the application in your web browser at:
`http://127.0.0.1:8000/`

# App Source


| Navigation | Description |
|------------|-------------|
| Rooms     | Explore, chat, collaborate, create, update, delete, organize, authenticate|
| Chat      | Messaging, moderation, restricts actions like deleting messages to authenticated users.|
| Qosyl(main)| Integrates multiple apps   |
| Base      | Search, overview, activity feed|
| Users      | Profiles(view, update, and manage their profiles), networking, insights|




# App Description
This project is a comprehensive social collaboration platform designed to connect users through shared interests, foster communication, and enable productive networking. It integrates various functionalities into a unified system, providing users with tools for discussion, learning, and personal interaction.

# Key Features:
User Management:

User authentication (login, registration, and logout).
Profile creation and management, including avatars and bio updates.
Friend requests, adding friends, and managing connections.
Rooms and Discussions:

Create, update, and delete discussion rooms on specific topics.
Search for rooms by topic, name, or description.
Participate in discussions through messaging and activity feeds.
Messaging:

Real-time chat functionality within rooms.
Manage and delete messages with permissions.
Activity page to review recent communications.
Topics and Discovery:

Explore trending topics and categories.
Search for relevant content and discussions.
Analytics and Insights:

Track user activities, such as messages and room participation.
Provide data visualization for user interactions and room engagements.
Networking:

Build a network of friends and interact with them through profiles and shared activities.

# Project Preview

......Place for photo of project(by parts).....
![Снимок экрана (48)](https://github.com/user-attachments/assets/b0128649-cbae-4726-9987-9ea1c728e2ae)
![Снимок экрана (38)](https://github.com/user-attachments/assets/65497e9a-9264-4bde-afb5-83881955ff6a)
![Снимок экрана (39)](https://github.com/user-attachments/assets/bbbd857d-e917-46fb-854b-dd604b265374)
![Снимок экрана (40)](https://github.com/user-attachments/assets/f6e52556-9d7b-4b6d-ac0d-29a8f7ebcbb7)
![Снимок экрана (41)](https://github.com/user-attachments/assets/9cb7efd8-2d8b-4997-8114-f53c93cd69ad)
![Снимок экрана (42)](https://github.com/user-attachments/assets/845f2ae1-8756-4ec1-9f96-979e65f57c84)
![Снимок экрана (43)](https://github.com/user-attachments/assets/5b738c8a-7ab4-48ed-b059-9cd95424a048)
![Снимок экрана (44)](https://github.com/user-attachments/assets/f54998fa-ca63-4ed6-a040-72f27fc1e2d2)
![Снимок экрана (45)](https://github.com/user-attachments/assets/3854014b-1d75-4f6a-87c8-0c716367a060)
![Снимок экрана (46)](https://github.com/user-attachments/assets/7f13b5c8-0b04-47fe-adf8-385cd6c2f980)
![Снимок экрана (47)](https://github.com/user-attachments/assets/26636b62-321c-4ad3-a14a-7c8fe33a664c)











# Project Members
| Full Name | ID |
|------------|-------------|
|  Kuanyshbekov Madi  | 22B030384   |
|   |     |
|  Akhanayeva Aruzhan  | 22B030516   |
|   |     |
|  Zeinolla Dilnaz  | 22B031177    |
|   |     |
|  Nurgaliev Dias  | 22B031188   |





# Used Topics at This Time

| Technical Side |  Topics Covered |
|------------|-------------|
| Models   |   ✓  |
| Views  |   ✓   |
| Templates  |   ✓   |
| DRF  |    ✓   |
| Session Management & Authentication  |    ✓   |
| Database |  ✓   |
| API  |   ✓   |
| Session Management & Authentication   |   ✓   |
| Analytical Component  |    ✓   |
| Logging  |    ✓   |
| Testing |  ✓   |



****

****
