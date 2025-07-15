# Dance Teaching Website 💃

A professional website for selling dance teaching packages with protected video access, user registration, gallery, and admin control – built with Django & Bootstrap.

## 🔗 Live Demo
👉 [https://bahadorleo.pythonanywhere.com](https://bahadorleo.pythonanywhere.com)

## 📸 Screenshots
<div align="center">
  <img src="contactes.jpg" width="600" alt="Homepage" />
  <img src="gallery.jpg" width="600" alt="Store Page" />
  <img src="home.jpg" width="600" alt="Package Detail" />
  <img src="my purchases.jpg" width="600" alt="My Packages" />
  <img src="phone1.jpg" width="600" alt="Contact Page" />
  <img src="phone2.jpg" width="600" alt="Contact Page" />
</div>

## ⚙ Features

- 🖼 Gallery with album/category support
- 💳 Video packages with secure purchase and streaming (no download)
- 🔒 Login & Register pages (authentication)
- 🧾 User dashboard: "My Packages"
- 📬 Contact form + Admin-editable social media links
- 📱 Responsive mobile-friendly UI (RTL design)

## 🛠 Tech Stack

- Django 4.2 (Python 3.8)
- Bootstrap 5 (RTL)
- SQLite3
- Hosted on PythonAnywhere (paid tier)

## 🚀 Getting Started (Dev Mode)

```bash
git clone https://github.com/bahadorsfq/dance_site.git
cd dance_site
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


🩰 Dance Training Website
A full-featured Persian-language website built with Django, designed for an online dance instructor. It provides video course packages, image galleries, music collections, user registration, purchase history, and admin-managed content — all presented with a responsive, mobile-friendly design.

🌟 Features
🛍️ Store Page: List and preview training packages with images, descriptions, and prices

💾 Secure Video Streaming: Purchased packages show video content only to the respective user — no downloads

📸 Gallery Section: Admin-uploaded categorized photo albums

🎵 Oriental Music Page: Collection of music tracks, editable via admin

👤 User Registration/Login: Custom login and registration system

💼 Admin Panel: Manage packages, users, galleries, music, and more

💬 Contact Page: Form and contact info managed from admin

📱 Responsive Design: Optimized for desktop and Android mobile devices

📸 Screenshots
Home Page	Store Page	My Purchases

Login	Gallery	Package Detail

⚙️ Technologies Used
Python 3.8+

Django 4.2

SQLite

HTML5, Bootstrap 5 (RTL)

Deployed on PythonAnywhere

📁 Project Structure
csharp
Copy code
dance_site/
├── core/               # Gallery, contact, about
├── store/              # Store, purchase logic, registration
├── templates/
│   ├── base.html       # Global layout
│   ├── store/          # Store templates
│   └── core/           # Gallery, contact, about
├── media/              # Uploaded videos and images
├── static/             # Static files (CSS/JS)
└── db.sqlite3
🧑‍💻 Developer
This project was built with ❤️ by Bahador Sfq
Want to hire me? Get in touch.