
✈️ Travel Booking Website

A full-stack travel booking platform where users can browse available flights, create reservations, and receive payment instructions online.
This project was built for a travel agency to improve customer experience and simplify the booking process.
live now on https://judandjurry.onrender.com
⸻

🚀 Features
	•	🔐 Authentication System – Users must register and sign in before making reservations.
	•	🛫 Flight Browsing – Clients can search and view available flights.
	•	📝 Reservation Flow – Users enter passenger details to create a reservation.
	•	📊 Summary Page – Displays total price and number of passengers, with an optional promo code input for discounts (if available).
	•	💳 Payment Instructions – No direct online payments. Instead, the site provides payment details (Baridi Mon / CCP). Clients then send proof of payment via WhatsApp.
	•	📩 Newsletter CTA – A section where users can subscribe for updates.

⸻

🛠️ Tech Stack
	•	Frontend: HTML, CSS, JavaScript , Bootstrap5
	•	Backend: Django
	•	Database: PostgreSQL

⸻

📂 Installation & Setup
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


🔮 Future Improvements
	•	Add a real online payment gateway (Stripe, PayPal, etc.).
	•	Implement an admin dashboard for managing flights and reservations.
	•	Enhance UI with React or Next.js.
