# ✈️ Travel Booking Website

A full-stack flight reservation platform where users can browse flights, create reservations, and receive payment instructions online.  
This project was built for a travel agency to improve customer experience and simplify the booking process.  

🔗 **Live Demo:** [judandjurry.onrender.com](https://judandjurry.onrender.com)

---

## 🚀 Features
- **Authentication System** – Users must register and log in before making reservations.  
- **Flight Browsing** – Clients can search and view available flights.  
- **Reservation Flow** – Users enter passenger details to create a reservation.  
- **Summary Page** – Displays total price, number of passengers, and an optional promo code input for discounts.  
- **Payment Instructions** – Instead of online payments, users receive details (Baridi Mon / CCP) and send proof via WhatsApp.  
- **Newsletter CTA** – Subscription form for updates.  

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5  
- **Backend:** Django  
- **Database:** PostgreSQL  

---

## 📂 Installation & Setup

```bash
# Clone this repository
git clone https://github.com/Houria-hs/travel-website.git

# Navigate into the project folder
cd travelwebsite

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver

