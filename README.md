# RecRoot

**RecRoot** is an open-source, unofficial backend server for Rec Room (2021 build), written in Python.  
This project is a non-commercial revival effort — not affiliated with or endorsed by Against Gravity.

---

## ✨ Features

- JWT authentication
- In-memory caching (thread-safe)
- CORS support
- Rate limiting
- Avatar items, consumables & equipment endpoints
- Game configs & room import support
- WebSocket support (planned)

---

## 📁 Project Structure

```
RecRoot/
├── main.py               # Entry point
├── requirements.txt      # Python dependencies
├── config/
│   └── settings.py       # Server configuration
├── core/
│   ├── auth.py           # JWT authentication
│   ├── cache.py          # In-memory cache
│   └── rate_limiter.py   # Rate limiting middleware
├── routes/
│   ├── account.py        # Account & login endpoints
│   ├── avatar.py         # Avatar items & equipment
│   ├── config.py         # ConfigV2 & GameConfigs
│   ├── rooms.py          # Room import & management
│   └── consumables.py    # Consumables & inventory
├── realtime/
│   └── ws_server.py      # WebSocket server (planned)
├── data/
│   └── README.md         # Static data files (JSON configs)
└── docs/
    └── api.md            # API endpoint documentation
```

---

## 🚀 Getting Started

### Requirements

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/ilfigliodiele/RecRoot.git
cd RecRoot
pip install -r requirements.txt
```

### Running the server

```bash
python main.py
```

By default the server runs on `http://0.0.0.0:5000`.

---

## ⚙️ Configuration

Edit `config/settings.py` to change:

- Port
- JWT secret key
- Rate limit thresholds
- CORS origins

---

## 📡 Supported Client

Designed to work with the original compiled Rec Room client (2021 build, PC/Steam).

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

---

## ⚠️ Disclaimer

This is a non-commercial fan revival project.  
RecRoot is not affiliated with, endorsed by, or connected to Against Gravity or Rec Room.  
All Rec Room assets and trademarks belong to Against Gravity.

---

## 💾 Depot Manifest

5515810233259164887

---

## 📄 License

MIT — see [LICENSE](LICENSE)
