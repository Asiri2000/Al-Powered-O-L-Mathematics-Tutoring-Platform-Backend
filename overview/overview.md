# AI-Powered O/L Mathematics Tutoring Platform — System Overview

> **Last Updated:** 2026-04-12  
> **Purpose:** Reference document for developers to understand system architecture, components, data flow, and service boundaries.

---

## 1. Project Summary

This is an AI-powered personalised learning platform built specifically for **Sri Lankan G.C.E. O/Level mathematics students (Grades 10–11)**. The system's core research goal is to:

- Provide **adaptive, personalised tutoring** based on student performance
- **Identify learning risk periods** such as knowledge gaps, conceptual misunderstandings, and skill insufficiency
- Deliver **curriculum-accurate content** aligned with the Sri Lankan GCE O/L mathematics syllabus

---

## 2. High-Level Architecture

The platform is composed of **five main layers** communicating via REST APIs:

```
┌──────────────────────────────────────────────────────────┐
│                   FrontEnd (React + Vite)                │
│          User Interface — Runs on browser                │
└──────────────────────┬───────────────────────────────────┘
                       │  HTTP REST (port 5080)
                       ▼
┌──────────────────────────────────────────────────────────┐
│              BackEnd (Node.js / Express)                 │
│     Auth, Users, Quiz, Analytics, Diagnosis, Dashboard   │
│                 PostgreSQL via Sequelize                 │
└───────────┬──────────────────────────┬───────────────────┘
            │                          │
   HTTP REST │                HTTP REST │
            ▼                          ▼
┌──────────────────────┐   ┌──────────────────────────────┐
│    Agent Service     │   │        RAG Service           │
│  (Python / FastAPI)  │   │     (Python / FastAPI)       │
│  CrewAI Agents +     │   │  LangChain + FAISS + OpenAI  │
│  Adaptive Engine     │◄──│  Grade10/11 Math Textbook    │
└──────────────────────┘   └──────────────────────────────┘
            │
            ▼
┌──────────────────────────────────────────────────────────┐
│                  Chatbot Service                         │
│             (Node.js + Google Gemini API)                │
│            Standalone: general + math Q&A               │
└──────────────────────────────────────────────────────────┘
```

---

## 3. Module Breakdown

### 3.1 FrontEnd (`/FrontEnd`)

**Technology:** React 19, Vite 7, TailwindCSS 4, React Router DOM 7, Framer Motion, Axios

**Entry Point:** `FrontEnd/src/main.jsx` → `App.jsx`

#### Routing (`App.jsx`)

| Route | Component | Role |
|---|---|---|
| `/` | `Home` | Landing page |
| `/login` | `Login` | Student login form |
| `/signup` | `Signin` | Student registration |
| `/generator` | `QuestionGenerator` | AI quiz question generator |
| `/companion` | `LearningCompanion` | AI learning companion chat |
| `/performance` | `Performance` | Student performance analytics |
| `/lessons` | `Lessons` | Lesson browser |
| `/lesson/:id` | `LessonCompanion` | Individual lesson with AI help |
| `/admin` | `AdminPage` | Admin dashboard |
| `/admin/users` | `UserDetails` | Admin: view/manage users |
| `/admin/add-content` | `AddContent` | Admin: add questions/content |

#### Shared Components

- `Navbar.jsx` — Global navigation bar
- `Footer.jsx` — Global footer
- `CelebrationOverlay.jsx` — Animated reward overlay on correct answers
- `slides/` — Slide-based components

#### API Layer (`src/api.js`)

A centralized Axios instance targeting `http://127.0.0.1:5080/api`. Attaches JWT from `sessionStorage` (key: `accessToken`) on every request.

**Exported API calls:**

| Function | Method | Endpoint |
|---|---|---|
| `registerUser` | POST | `/auth/register` |
| `loginUser` | POST | `/auth/login` |
| `getCurrentUser` | GET | `/users/profile` |
| `getAllUsers` | GET | `/users` |
| `deleteUser` | DELETE | `/users/:id` |
| `updateUserRole` | PUT | `/users/:id/role` |
| `getChapterAnalytics` | GET | `/analytics/chapters` |
| `getOverallSummary` | GET | `/analytics/summary` |
| `getErrorBreakdown` | GET | `/diagnosis/errors` |
| `getWeakChapters` | GET | `/diagnosis/weaknesses` |
| `generateQuiz` | POST | `/quiz/generate` |
| `submitQuizAttempt` | POST | `/quiz/submit` |

---

### 3.2 BackEnd (`/BackEnd`)

**Technology:** Node.js, Express 4, Sequelize 6 ORM, PostgreSQL (`pg`), JWT (`jsonwebtoken`), bcrypt, Nodemailer, Helmet, Morgan

**Entry Point:** `BackEnd/src/server.js` → `app.js`

#### API Routes

| Prefix | Router File | Description |
|---|---|---|
| `/api/auth` | `authRoutes.js` | Register, Login |
| `/api/users` | `userRoutes.js` | Profile, admin CRUD |
| `/api/questions` | `questionRoutes.js` | Question bank management |
| `/api/tutors` | `tutorRoutes.js` | Tutor/AI content endpoints |
| `/api/quiz` | `quizRoutes.js` | Generate & submit quiz |
| `/api/analytics` | `analyticsRoutes.js` | Chapter-level performance stats |
| `/api/diagnosis` | `diagnosisRoutes.js` | Weak area & error analysis |
| `/api/dashboard` | `dashboardRoutes.js` | Summary dashboard data |

#### Controllers

| File | Responsibility |
|---|---|
| `authController.js` | Register, Login, JWT issuance |
| `userController.js` | Profile management, admin user CRUD |
| `questionController.js` | CRUD for math questions |
| `quizController.js` | Quiz generation, attempt submission |
| `analyticsController.js` | Performance aggregation |
| `diagnosisController.js` | Weakness detection, error patterns |
| `tutorController.js` | Tutor interaction logs |
| `dashboardController.js` | Holistic dashboard summary |

#### Database Models (Sequelize / PostgreSQL)

| Model | Table | Key Fields |
|---|---|---|
| `User` | `users` | `id` (UUID), `studentName`, `username`, `email`, `password`, `grade`, `school`, `role` |
| `Question` | `questions` | Question data and metadata |
| `QuizAttempt` | `quiz_attempts` | `user_id`, `question_id`, `chapter`, `question`, `selected_answer`, `correct_answer`, `is_correct`, `time_taken` |
| `ChapterMastery` | `chapter_mastery` | `user_id`, `chapter`, `mastery_level`, `accuracy`, `avg_time`, `difficulty_level`, `total_attempts` |
| `Session` | `sessions` | JWT session tracking |
| `Tutor` | `tutors` | Tutor entity |

#### Middleware

| File | Purpose |
|---|---|
| `authMiddleware.js` | JWT verification on protected routes |
| `errorHandler.js` | Central error response formatter |
| `validation.js` | Request body validation rules |

#### Services

| File | Purpose |
|---|---|
| `aiService.js` | HTTP proxy calls to the AI Agent service (`/process`, `/solve`) |
| `diagnosisService.js` | Logic for diagnosing student weak areas |
| `emailService.js` | Nodemailer email notifications |
| `mathService.js` | Supporting math utilities |

#### Environment Variables (`.env.example`)

```
DATABASE_URL=        # PostgreSQL connection string
JWT_SECRET=          # JWT signing secret
PORT=3000
NODE_ENV=development
EMAIL_SERVICE=
EMAIL_USER=
EMAIL_PASS=
```

---

### 3.3 Agentic AI Agents (`/agentic_AI_agents`)

This directory houses **two Python microservices**, both using FastAPI.

---

#### 3.3.1 Agent Service (`/agentic_AI_agents/agent-service`)

**Technology:** Python, FastAPI, CrewAI, Pydantic, SQLAlchemy, psycopg2, requests

**Entry Point:** `api/main.py` (FastAPI app)

##### API Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/generate-quiz` | Generate a static quiz question |
| POST | `/generate-adaptive-quiz` | Generate a difficulty-adjusted adaptive question |

##### Agents (CrewAI)

| Agent File | Role | Purpose |
|---|---|---|
| `quiz_agent.py` | GCE O/L Mathematics Examiner | Generate syllabus-accurate MCQ questions |
| `diagnosis_agent.py` | Error Analyst | Diagnose student mistakes and misconceptions |
| `analytics_agent.py` | Analytics Agent | Analyse performance data |
| `personalization_agent.py` | Personalization Agent | Adapt learning plans |
| `mock_exam_agent.py` | Mock Exam Creator | Generate full mock exam sets |
| `tutor_agent.py` | Tutor Agent | Provide tutoring explanations |

##### Crews (CrewAI Crew compositions)

| Crew File | Agents Used | Purpose |
|---|---|---|
| `learning_crew.py` | DiagnosisAgent | Builds a crew with a diagnosis task based on chapter analytics |
| `quiz_crew.py` | QuizAgent | Generates quiz questions |
| `mock_exam_crew.py` | MockExamAgent | Generates mock exams |
| `tutor_feedback_crew.py` | TutorAgent | Provides tutoring feedback |

##### Tasks

| Task File | Purpose |
|---|---|
| `quiz_task.py` | Task definition for quiz generation |
| `mock_exam_task.py` | Task definition for mock exam generation |
| `tutor_feedback_task.py` | Task definition for tutor feedback |

##### Adaptive Learning Services (Orchestration Layer)

| Service File | Purpose |
|---|---|
| `adaptive_quiz_orchestrator.py` | Master orchestrator: determines mastery stage, adjusts difficulty, selects action, generates question |
| `difficulty_engine.py` | Adjusts difficulty level based on accuracy + average response time |
| `progression_engine.py` | Determines learning stage (e.g., beginner, developing, mastery) |
| `learning_orchestrator.py` | Decides learning actions (practice more, advance, remediate) |
| `decision_engine.py` | Simplified decision logic |
| `learning_decision_engine.py` | Extended learning decision rules |
| `remediation_service.py` | Provides remediation steps for weak students |
| `topic_generators.py` | Maps topics to question generation logic |
| `diagram_factory.py` | Generates diagram-based question descriptions |
| `registry.py` | Routes grade+topic to the appropriate question generator |

##### Tools (used by agents)

| Tool File | Purpose |
|---|---|
| `rag_tool.py` | Queries the RAG service for syllabus-accurate textbook answers |
| `analytics_tool.py` | Fetches chapter analytics from the BackEnd API (using JWT) |
| `db_tool.py` | Direct database access utility |

##### Key Config (`config.py`)

```python
OPENAI_API_KEY   # LLM access
RAG_API_URL      # URL of the RAG service
BACKEND_API_URL  # URL of the Node.js BackEnd
JWT_TOKEN        # Service-to-service auth token (AGENT_JWT_TOKEN)
```

---

#### 3.3.2 RAG Service (`/agentic_AI_agents/rag-service`)

**Technology:** Python, FastAPI, LangChain, FAISS (CPU), OpenAI Embeddings (`text-embedding-3-small`), GPT-3.5-Turbo, PyPDF

**Entry Point:** `main.py`

##### What it does

1. On **startup**: Ingests `grade10_11_math.pdf` (27 MB, Sri Lankan O/L math textbook) into a FAISS vector store
2. At **runtime**: Accepts natural language queries and returns answers grounded in the textbook

##### API Endpoints

| Method | Path | Request | Response |
|---|---|---|---|
| POST | `/retrieve` | `{ "query": string }` | `{ "answer": string, "context": [string] }` |

##### Internal Pipeline

```
User Query
    ↓
FAISS Vector Store  ←  grade10_11_math.pdf (chunked & embedded)
    ↓ (top-k documents)
LangChain RAG Chain
    ↓ (GPT-3.5-Turbo)
Answer + Source Context
```

---

### 3.4 Chatbot (`/chatbot`)

**Technology:** Node.js, Express, Google Generative AI SDK (`@google/generative-ai`), Gemini API

**Entry Point:** `chatbot/server.js`

**Purpose:** A **standalone conversational chatbot** for general math Q&A, embedded via the `index.html` chat UI.

#### Key Features

- Connects to **Google Gemini API** (`gemini-1.5-flash-latest` or fallback models)
- If input looks like a **quadratic equation**, it is solved **deterministically** (no LLM), e.g. `2x^2+3x-5=0`
- For all other math/general queries, delegates to Gemini with temperature 0 (math) or 0.9 (general)
- Model fallback chain: tries multiple Gemini model variants until one responds

#### API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Serves the chatbot HTML UI |
| GET | `/models` | Lists available Gemini models |
| POST | `/chat` | Accepts `{ userInput }`, returns `{ response, source }` |

#### Environment Variables

```
API_KEY=         # Google Gemini API key
PORT=3000
MODEL_NAME=      # Default: gemini-1.5-flash-latest
MATH_SOLVER_ENABLED=  # Default: true (enables deterministic quadratic solver)
```

---

## 4. Data Flow — End-to-End Quiz Generation

```
Student (FrontEnd)
  │ POST /quiz/generate  { grade, topic, difficulty }
  ▼
BackEnd (Node.js)
  │ → quizController calls agentService
  │ POST /generate-adaptive-quiz to Agent Service
  ▼
Agent Service (FastAPI)
  ├── progression_engine: determine mastery stage
  ├── difficulty_engine: adjust difficulty
  ├── learning_orchestrator: decide action
  ├── registry: get topic generator
  └── generator: generate question using CrewAI QuizAgent + OpenAI
        │
        └── [optionally] rag_tool: query RAG service for textbook context
              ▼
          RAG Service (FAISS + GPT-3.5)
              returns answer/context
  ▼
Question returned → BackEnd → FrontEnd renders MCQ
  │
  ▼
Student answers → POST /quiz/submit
  ▼
BackEnd stores QuizAttempt + updates ChapterMastery
  ▼
Analytics available at /analytics/chapters, /diagnosis/weaknesses
```

---

## 5. Service Port Reference

| Service | Runtime | Default Port |
|---|---|---|
| FrontEnd (Vite dev) | Node.js | `5173` (Vite default) |
| BackEnd API | Node.js | `5080` (configured in frontend api.js) |
| Agent Service | Python/Uvicorn | TBD (configured via `BACKEND_API_URL`) |
| RAG Service | Python/Uvicorn | TBD (configured via `RAG_API_URL`) |
| Chatbot | Node.js | `3000` |

---

## 6. Authentication Model

- **JWT-based** authentication for both users and service-to-service calls
- User tokens issued at login, stored in `sessionStorage` (`accessToken`)
- Agent service uses a **dedicated service JWT** (`AGENT_JWT_TOKEN`) for calling BackEnd endpoints (not a user token)
- Admin role vs. student role controlled by `role` field in the `User` model
- The `generateAgentToken.js` script in BackEnd root is used to manually generate agent service tokens

---

## 7. Key Technology Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Agentic AI Framework | **CrewAI** | Role-based multi-agent orchestration for complex workflows |
| LLM for Agents | **OpenAI GPT** (via CrewAI) | High accuracy for structured output |
| Chatbot LLM | **Google Gemini** | Free tier for conversational UI |
| RAG Embeddings | **OpenAI text-embedding-3-small** | High quality, cost efficient |
| Vector Store | **FAISS (CPU)** | Offline, fast local retrieval |
| Backend ORM | **Sequelize** | PostgreSQL interface |
| Frontend Build | **Vite + React** | Fastest development experience |
| Curriculum Source | **grade10_11_math.pdf** | Official Sri Lankan O/L math textbook |

---

## 8. Directory Tree

```
AI-Powered-O-L-Mathematics-Tutoring-Platform/
│
├── overview/                          ← This document
│   └── overview.md
│
├── FrontEnd/                          ← React 19 + Vite SPA
│   └── src/
│       ├── App.jsx                    ← Router config
│       ├── api.js                     ← Centralized Axios API layer
│       ├── pages/
│       │   ├── user/                  ← Student-facing pages
│       │   │   ├── Home.jsx
│       │   │   ├── login.jsx
│       │   │   ├── signin.jsx
│       │   │   ├── learningCompanion.jsx
│       │   │   ├── lessonCompanion.jsx
│       │   │   ├── lessons.jsx
│       │   │   ├── questionGenerator.jsx
│       │   │   └── Performance.jsx
│       │   └── admin/                 ← Admin pages
│       │       ├── adminPage.jsx
│       │       ├── UserDetails.jsx
│       │       └── AddContent.jsx
│       └── components/
│           ├── Navbar.jsx
│           ├── Footer.jsx
│           └── CelebrationOverlay.jsx
│
├── BackEnd/                           ← Node.js / Express API
│   └── src/
│       ├── app.js                     ← Express setup + route mounting
│       ├── server.js                  ← HTTP server start
│       ├── config/                    ← DB config
│       ├── controllers/               ← Request handlers
│       ├── models/                    ← Sequelize ORM models
│       ├── routes/                    ← Express routers
│       ├── middleware/                ← Auth, error, validation
│       ├── services/                  ← AI, email, math, diagnosis
│       └── utils/
│
├── agentic_AI_agents/
│   ├── agent-service/                 ← CrewAI + FastAPI Agent microservice
│   │   ├── api/main.py                ← FastAPI entry point
│   │   ├── agents/                    ← CrewAI agent definitions
│   │   ├── crews/                     ← CrewAI crew builders
│   │   ├── tasks/                     ← CrewAI task definitions
│   │   ├── services/                  ← Adaptive orchestration engines
│   │   ├── generators/                ← Question generators by topic/grade
│   │   ├── tools/                     ← RAG, analytics, DB tools
│   │   ├── prompts/                   ← LLM prompt templates
│   │   ├── schemas/                   ← Pydantic schemas
│   │   └── config.py                  ← API keys and service URLs
│   │
│   └── rag-service/                   ← RAG microservice (FAISS + LangChain)
│       ├── main.py                    ← FastAPI entry point
│       ├── ingest.py                  ← PDF ingestion to FAISS
│       ├── vector_store.py            ← FAISS search + LLM chain
│       ├── grade10_11_math.pdf        ← Source textbook (27 MB)
│       └── faiss_index/               ← Saved FAISS vector index
│
└── chatbot/                           ← Standalone Gemini-based chatbot
    ├── server.js                      ← Express + Gemini integration
    ├── index.html                     ← Chat UI
    └── loader.gif
```

---

## 9. Development Notes

### Starting the Services

```bash
# FrontEnd
cd FrontEnd && npm run dev

# BackEnd
cd BackEnd && npm run dev

# Agent Service (Python)
cd agentic_AI_agents/agent-service && uvicorn api.main:app --reload --port 8000

# RAG Service (Python)
cd agentic_AI_agents/rag-service && uvicorn main:app --reload --port 8001

# Chatbot
cd chatbot && node server.js
```

### Environment Setup Requirements

- **PostgreSQL** database running and accessible
- **OpenAI API key** (for Agent Service + RAG Service)
- **Google Gemini API key** (for Chatbot)
- **Service JWT token** generated via `BackEnd/generateAgentToken.js` and placed in `agent-service/.env` as `AGENT_JWT_TOKEN`

---

## 10. Research Context

This platform is built as part of a **research project** to study AI-powered personalised mathematics tutoring for Sri Lankan O/Level students. Core research problems addressed:

1. **Knowledge gap detection** — Identifying which chapters/topics a student is weak in
2. **Adaptive difficulty** — Dynamically adjusting question difficulty based on accuracy + response time
3. **Learning stage determination** — Classifying students into mastery progression stages
4. **Misconception diagnosis** — Using AI agents to explain *why* a student got something wrong
5. **Curriculum alignment** — Ensuring all AI-generated content strictly follows the Sri Lankan GCE O/L math syllabus

---

*This document was auto-generated by reviewing all source files across FrontEnd, BackEnd, agentic_AI_agents, and chatbot modules.*
