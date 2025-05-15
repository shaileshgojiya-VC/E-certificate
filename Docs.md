# 📜 API Documentation
> This Docs is for the reference purpose only

## 🔑 Authentication API
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/v1/user/register` | Registers a new user |
| POST | `/api/v1/user/login` | Authenticates user credentials |
| POST | `/api/v1/user/logout` | Logs out the user |
| POST | `/api/v1/user/forgot-password` | Sends password reset link |
| POST | `/api/v1/user/reset-password` | Resets password after verification |

---

## 🎭 Client Event Management API
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/v1/client/events` | Fetches all events |
| GET | `/api/v1/client/events/{event_id}` | Fetches details of a specific event |
| POST | `/api/v1/client/events` | Creates a new event |
| PUT | `/api/v1/client/events/{event_id}` | Updates an event |
| DELETE | `/api/v1/client/events/{event_id}` | Deletes an event |

---

## 🎟️ Booking API
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/v1/user/bookings` | Books an event seat |
| GET | `/api/v1/user/bookings/{booking_id}` | Retrieves booking details |
| PUT | `/api/v1/user/bookings/{booking_id}` | Updates seat selection |
| DELETE | `/api/v1/user/bookings/{booking_id}` | Cancels a booking |

---

## 💰 Payment API
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/v1/payments` | Processes event booking payments |

---

## 👤 User Profile API
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/v1/users/{user_id}` | Fetches user profile details |
| PUT | `/api/v1/users/{user_id}` | Updates user profile details |
| DELETE | `/api/v1/users/{user_id}` | Soft deletes a user account |

---

## 👨‍💼 Admin API
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/v1/admin/dashboard` | Fetches admin analytics |
| GET | `/api/v1/admin/clients` | Fetches all clients |
| POST | `/api/v1/admin/clients/add` | Adds a new client |
| DELETE | `/api/v1/admin/clients/{client_id}` | Removes a client |

---

## 🔄 API Workflow
1. **User Authentication**: User registers, logs in, and receives JWT token.
2. **Event Browsing**: Users fetch event listings and view event details.
3. **Booking Process**: Users book seats and receive confirmation.
4. **Payment Processing**: Users proceed to payment for their booked seats.
5. **Admin & Client Actions**: Admin manages clients, clients manage events.

---

📌 For more details, check the interactive API documentation at `/docs`. 🚀

