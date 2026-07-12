**For installation instructions, please scroll down.

# PaperGen

A Paper Generator tailored for generating randomized question papers for Indian school students.

#  What is it?

PaperGen is an application that generates test papers for various subjects like Physics, Chemistry, Biology, Mathematics, and Computer Science with respect to the selected class, chapters, board, and subject. It does all this locally without any internet access, which is a useful feature for regions where connectivity is a real problem.

Unlike AI models or other applications, which usually fail to understand the regional syllabus of Indian boards like CBSE, ICSE, and different State boards, PaperGen stores a database containing a huge amount of questions and answers from trusted sources and regional board syllabi. It is free and open-source under the GNU GPL license, so anyone can contribute to or modify it according to their usage and needs.
The Problem

In India, a huge population does not possess stable internet connections like Wi-Fi or routers; many of them are dependent either on limited cellular data or on their parents' or relatives' hotspots. Using online platforms for paper generation that require data or charge a premium can quickly become a problem.
The Solution

With PaperGen, students can create a bunch of new test papers to practice their knowledge of different subjects and prepare for upcoming exams. It does not require any internet connectivity or a bunch of complex applications. It can run on low-end devices (potato included) without any problem since it is really lightweight. The core files that generate and display the paper (i.e., excluding the database) have a file size of less than 1MB, making them suitable for low-storage devices.

# Key Features

- User-friendly UI

- Zero-network requirement

- Zero-dependency UI analytics screen

- Persistent storage: Stores the papers and results in an SQLite database, meaning the data will remain in your local storage

- Dynamic quiz generation: Can pull questions according to the entered criteria and generate an MCQ quiz

# Tech Stack Breakdown

* Backend Core: Python 3.x

* Database Layer: SQLite3

* Desktop Bridge Architecture: pywebview (for rendering native GUI app windows without massive frameworks like Electron)

* Frontend Interface: Vanilla HTML5, CSS3, and JavaScript (Zero external network calls)
# Installation Guide

-Install pywebview:

```pip install pywebview```

- Run main.py

```python3 main.py```

IMPORTANT: The exam_engine.db file must be located in the same file path.

# Future Plans

If I had two more weeks to work on this app, here is exactly what we would build next to make it ready for schools:

* Printable PDF Report Cards: Let students or teachers export their test results and pie charts into a clean, professional PDF file that they can print out or share offline.

* Profiles for Multiple Students: Add a simple login screen so different students or siblings can share the exact same app on a single home or school computer, keeping their test scores and histories completely separate.

* Offline AI Question Creator: Connect a small, lightweight AI model that runs completely locally on the device to automatically generate brand new math and science questions so the database never runs out.

    Full Subject & Board Catalog: Finish adding the question banks for ICSE and State Boards, along with extra subjects like Chemistry, Mathematics, and Computer Science.**
