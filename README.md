# Frosty

Frosty is a playground project that pairs a modern React + Vite frontend with a tiny Python echo server.
It showcases a docked chat UI (sidebar, history list, settings drawer, theme persistence) that talks to the
backend through a single `/echo` endpoint.

```
.
├── backend
│   └── server.py          # Threaded HTTP echo server with permissive CORS
└── frontend               # React 19 + TypeScript + Vite + Tailwind CSS app
    ├── src/components     # Chat surface, sidebar, settings dialog and UI primitives
    ├── src/lib            # Shared helpers (eg. classNames utility)
    └── vite.config.ts     # React compiler + Tailwind Vite plugins
```

## Requirements

- Node.js 20+ (comes with npm 10+)
- Python 3.10+ (used only for the lightweight backend)

## Setup

1. Install the frontend dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. Run the backend echo server in a separate terminal:

   ```bash
   cd backend
   python3 server.py
   ```

   The server listens on `http://127.0.0.1:8000/echo` and simply sends back whatever JSON payload you post.
   It already sets permissive CORS headers so the Vite dev server can reach it without proxies.

3. Start the Vite development server:

   ```bash
   cd frontend
   npm run dev
   ```

4. Visit the URL printed by Vite (typically `http://127.0.0.1:5173`) to interact with the UI.

## Usage Flow

1. Type a prompt in the “Ask Frosty” input. Press `Enter` to send or `Shift+Enter` to insert a newline.
2. Messages you send appear right-aligned (user role). The app immediately POSTs the content to `http://127.0.0.1:8000/echo`.
3. The backend responds with `{ "reply": "<same text>" }`; the frontend renders it as a left-aligned assistant message.
4. Use the hover controls on assistant messages to copy, thumbs up/down, or flag a response.
5. The sidebar contains a mock conversation list, account menu, and settings dialog (purely UI, no persistence yet).

Because the backend just echoes text, Frosty is ideal for UI work—swap in a real model/API by adjusting the request
inside `frontend/src/components/Chat.tsx`.

## Available Scripts

Inside `frontend/`:

- `npm run dev` – start Vite with Fast Refresh.
- `npm run build` – type-check, then create a production build in `dist/`.
- `npm run preview` – serve the build locally for smoke testing.
- `npm run lint` – run ESLint across the project.

Backend (`backend/server.py`) has no external dependencies; run it with any recent CPython interpreter.

## Production Build & Deployment

1. Build the frontend: `cd frontend && npm run build`.
2. Serve the `dist/` directory using any static host (Vercel, Netlify, S3 + CloudFront, etc.).
3. Keep the Python service running alongside the static assets (for example via `systemd`, Docker, or any PaaS).
   Update the frontend request URL if you host the backend somewhere other than `127.0.0.1:8000`.

## Customization Notes

- **API target** – Replace the hard-coded URL in `src/components/Chat.tsx` with an environment-aware value if
  you deploy to multiple stages.
- **Conversation list** – Edit `src/components/AppSidebar.tsx` to change the mock chat history data.
- **Branding & theme** – The Tailwind 4 token definitions live in `frontend/src/index.css`. Modify them or extend
  `ThemeProvider` if you need additional schemes.

## Verifying the Backend Independently

Use `curl` (or any HTTP client) to make sure the server responds before wiring up the UI:

```bash
curl -X POST http://127.0.0.1:8000/echo \
     -H "Content-Type: application/json" \
     -d '{"message":"Hello Frosty"}'
# → {"reply":"Hello Frosty"}
```

You should now have a fully working Frosty chat playground. Swap in another backend, connect real data, or keep
using it to iterate on conversational UI ideas.