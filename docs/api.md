# RecRoot API Documentation

Base URL: `http://localhost:5000`

---

## Authentication

All protected endpoints require a JWT token in the `Authorization` header:

```
Authorization: Bearer <token>
```

---

## Endpoints

### Auth

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/auth/login` | Login and receive JWT token |
| POST | `/api/auth/register` | Register a new account |

### Account

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/account/me` | Get current user info |

### Config

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/config/v2` | Get ConfigV2 |
| GET | `/api/config/game` | Get GameConfigs |

### Avatar

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/avatar/items` | Get all avatar items |
| GET | `/api/avatar/equipment` | Get equipment list |

### Consumables

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/consumables` | Get consumables catalog |

### Rooms

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/rooms` | List available rooms |
| POST | `/api/rooms/import` | Import a room |

---

## WebSocket (planned)

`ws://localhost:5001` — Realtime game server (replaces Photon)
