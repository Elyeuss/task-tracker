# My Task Tracker

A command-line task manager built with Python and Supabase. You can add, list, complete, and delete tasks, and they are saved in a cloud database.

## Setup

1. Create a free project at [supabase.com](https://supabase.com).
2. In the SQL Editor, run:

```sql
   create table tasks (
     id bigint primary key generated always as identity,
     title text not null,
     is_done boolean default false,
     created_at timestamptz default now()
   );
```

3. Create a `.env` file in the project folder:
SUPABASE_URL=your-project-url
SUPABASE_KEY=your-publishable-key

4. Create a virtual environment and install the packages:
python -m venv venv
venv\Scripts\activate
pip install supabase python-dotenv

## Run
venv\Scripts\activate
python main.py

## What I learned

- I learned how to create my own database related project from scratch and utilizing AI tools to help guide and give
input on where/how to approach problems. I learned how to document data into a database as well as where to create/use/access a database.
I learned how to create useful projects outside of ROBLOX.