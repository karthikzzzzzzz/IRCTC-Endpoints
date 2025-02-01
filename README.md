# Railway Management System API

This repository contains the implementation of a Railway Management System API. The API allows users to search for trains, check seat availability, book seats, and retrieve booking details. It also provides an admin interface for managing trains and seats.

---

## Features

- **User Registration**: Create new user accounts.
- **User Login**: Authenticate users and generate tokens for API access.
- **Train Management** (Admin Only):
  - Add new trains with source and destination stations.
  - Update the number of available seats for trains.
- **Train Search**:
  - Retrieve trains available between two stations.
  - View seat availability for the selected train.
- **Booking**:
  - Book seats on trains (handles race conditions for simultaneous bookings).
  - Retrieve booking details for a user.

---

## Tech Stack

- **Backend Framework**: Python (Flask/Django) / Node.js (Express) / Java (Spring Boot)
- **Database**: MySQL/PostgreSQL
- **Authentication**: API key for admin endpoints and JWT for user endpoints

---

## Prerequisites

Ensure the following are installed on your system:
- Python 3.x or Node.js / Java JDK
- MySQL/PostgreSQL
- Git

---

API Endpoints

User Endpoints
Register a User: POST /api/register
Login a User: POST /api/login
Search Trains: GET /api/trains?source={source}&destination={destination}
Book a Seat: POST /api/book
Get Booking Details: GET /api/bookings/{id}
Admin Endpoints (Protected by API Key)
Add a Train: POST /api/admin/trains
Update Train Seats: PATCH /api/admin/trains/{id}
Authentication

Admin APIs: Require an API key (x-api-key header).
User APIs: Require a JWT token (Authorization header).

