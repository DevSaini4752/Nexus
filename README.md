# 🌐 Nexus—Your Smart Terminal Gateway to the world
 
A powerful, modular, and extensible terminal-based assistant that empowers users with productivity tools, 
real-time data, and a personal task manager — all backed by a secure account system.

---

## 🚀 Features

Nexus isn’t your ordinary script — it’s a full ecosystem in your terminal. Here’s what it includes:

### 🔐 Account System
- Register, login, and reset password securely.
- Each user has an isolated `.json` data profile.
- Session-based data handling to reduce I/O overhead and simulate RAM-like storage during usage.

### 📰 News Aggregator
- Get personalized or general news.
- Fetch custom headlines by topic, or explore current affairs.
- API-powered for real-time updates.

### 🗞 Smart Newsletter
- Automatically sends a personalized daily newsletter to users.
- Includes top headlines according to your personalization.
- Built on the modular `Smart_Mail` system using account-level preferences

### 📈 Stock Market Analyzer
- Search any stock by symbol (e.g., TSLA, INFY).
- View current, historical, and custom date range data.
- Clean integration with financial data APIs.

### 💱 Currency Exchange Rates
- Get real-time exchange rates for any currency.
- Historical data back to 1999.
- Base currency: USD.

### 🌦️ Weather Forecast
- Live weather data for any location.
- Includes temperature, condition, and more.

### ✅ ToDo Manager (TDM)
A gamified productivity system with deadline tracking.

- Add tasks with deadlines.
- Smart point system:
  - +2 for initializing a task.
  - -2 if cancelled within 2 mins.
  - -6 for missing deadlines.
  - +8 for completing tasks.
- Modular & now upgraded for account-based task handling.

---

## 🧠 Architecture

- ✅ Modular Design – Over 20+ structured modules.
- 🔐 `.env` support for secure secrets (API keys and passwords).
- 🗂️ Data handling per user using `User_Accounts_TDM/` directory.
- ⚙️ Easily scalable for future additions like GUI or DB.

---

## 📂 Folder Structure (Simplified)

Nexus/<br>
├── main.py<br>
├── .env # Contains API keys (gitignored)<br>
├── example.env # Template for environment variables<br>
├── SmartMail/ # Modular emailing system<br>
├── modules/ # All feature modules (news, stocks, weather etc.)<br>
├── ToDoManager/ # Gamified task manager with account support<br>
├── UserAccounts.tdm/ # User-wise data folders<br>
└── README.md

---

## 🔐 Environment Variables
1. Duplicate the example.env file and rename it to .env
2. Fill in your own API keys and credentials
3. Use it as normal
- Using .env was the first initiative after I mistakenly uploaded the API keys
---

## ⚠ Important Notice

### 🔐 Security Advisory

Some earlier commits in this repository may contain exposed *API keys*.  
These keys have already been *revoked or regenerated, and **no longer pose any security risk*.

--

🛡 *From the latest updates onward*, this project follows  
*secure API key management practices* using more *robust and responsible methods*.

--

🧠 _This level of transparency is intentional and reflects the project's evolution_  
_toward real-world, secure software development standards._

---

## 🛠 Tech Stack

- **Language**: Python 3.11+
- **Libraries**: `requests`, `json`, `datetime`, `os`, `dotenv`, and more.
- **Tools**: Terminal-only; no GUI required.

---

## 💡 Vision

> What started as a simple API practice project turned into a modular, multi-feature, account-based system to help users stay informed, productive, and efficient.

---

## 👨‍💻 Developer
**Dev Saini**

---

## 📜 License

MIT License (or any you prefer — you can change this later)

