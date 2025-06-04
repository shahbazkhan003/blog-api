✅ Updated `README.md`

```markdown
# 📝 Blog API with Django REST Framework

This is a simple Blog API built using Django and Django REST Framework (DRF). It supports basic CRUD (Create, Read, Update, Delete) operations on blog posts, with support for post status (Draft or Published).

---

## 📦 Features

- Get all blog posts
- Retrieve a single blog post
- Create a new blog post with status (Draft/Published)
- Update an existing blog post
- Delete a blog post

---

📁 Project Structure

```

your\_project/
├── blog/                # Your app
│   ├── models.py        # Post model with status choices
│   ├── serializer.py    # PostSerializer
│   ├── views.py         # API views (List, Detail)
│   └── urls.py          # API routes
├── your\_project/        # Django project settings
│   └── settings.py
├── manage.py

````

---

🛠️ Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/your-username/blog-api.git
cd blog-api
````

2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Make sure your `requirements.txt` includes:

```
django
djangorestframework
```

3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run the Server

```bash
python manage.py runserver
```

---

 📮 API Endpoints

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| GET    | `/posts/`      | List all posts           |
| POST   | `/posts/`      | Create a new post        |
| GET    | `/posts/<pk>/` | Retrieve a specific post |
| PUT    | `/posts/<pk>/` | Update a specific post   |
| DELETE | `/posts/<pk>/` | Delete a specific post   |

---

 🔌 Example Request (POST)

```json
POST /posts/
Content-Type: application/json

{
  "title": "My First Blog Post",
  "content": "This is the content of the post.",
  "status": "published"
}
```

> `status` can be either `"draft"` or `"published"`.

---

 🧱 Models

 `Post`

| Field       | Type      | Description                                 |
| ----------- | --------- | ------------------------------------------- |
| id          | Integer   | Auto-generated primary key                  |
| title       | CharField | Title of the post (max length 200)          |
| content     | TextField | Content of the blog post                    |
| created\_at | DateTime  | Timestamp when post was created             |
| status      | CharField | `"draft"` or `"published"` (default: draft) |

---

 📦 Serializer

 `PostSerializer`

Serializes the `Post` model to and from JSON format.

---
