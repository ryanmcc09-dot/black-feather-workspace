# Multi-Agent Dashboard Operating System

**Status:** Master Plan Phase | **Created:** 2026-03-21 | **Owner:** Ryan McCormick

---

## Mission

Build a web-based command center where OpenClaw agents collaborate, hold meetings, track projects, and Ryan can observe everything in real-time. Two separate businesses (Music + Blog/Gaming) with Poe overseeing both.

---

## Architecture Overview

```
[Single Dashboard - Next.js + Convex]
         ↓
    ┌────┴────┐
    ↓         ↓
[Gateway 1] [Gateway 2]
  Music       Blog/Gaming
    ↓           ↓
  Chester    Shepherd
  Runefury    Content
  Marketing   Research
              Editor
              Marketing
```

---

## Data Storage Map

### **Convex Cloud (Free Tier - 1GB)**
*Structured data requiring real-time sync and queries*

| Data Type | Why Convex | Estimated Size |
|-----------|------------|----------------|
| Articles database | Query by game/topic before writing | ~50KB (1000 articles) |
| Research materials registry | Prevent researcher duplication | ~100KB |
| Agent communication logs | Real-time chat between agents | ~500MB (text only) |
| Meeting transcripts | Searchable, queryable | ~200MB |
| Project tracking metadata | Status, assignments, deadlines | ~50KB |
| Marketing content calendar | Scheduling, approval workflow | ~100KB |
| Chester Studio metadata | Lyrics, song info, release dates | ~50KB |
| Authentication users | Login sessions, permissions | ~10KB |

### **GMKtek Local Storage (1TB SSD)**
*Large files and raw content*

| Data Type | Location |
|-----------|----------|
| Audio files (music) | `/data/chester/audio/` |
| Video files | `/data/marketing/video/` |
| Article markdown files | `/data/shepherd/articles/` |
| Research documents | `/data/shepherd/research/` |
| Agent session logs | `/data/agents/sessions/` |
| Dashboard app | `/data/dashboard/` |
| OpenClaw Gateway | `/data/openclaw/` |

---

## Convex Schema Design

### **1. Articles Collection**
```typescript
{
  _id: "article_123",
  businessId: "blog-gaming", // or "music"
  gameName: "Mordheim",
  topic: "New Faction Release",
  status: "researched" | "writing" | "editing" | "published",
  researcherId: "agent_researcher_1",
  writerId: "agent_writer_1",
  editorId: "agent_editor_1",
  researchMaterials: ["research_001", "research_002"],
  articlePath: "/data/shepherd/articles/mordheim-new-faction.md",
  createdAt: 1711068000000,
  publishedAt: null,
  tags: ["mordheim", "faction", "news"]
}
```

### **2. Research Materials Collection**
```typescript
{
  _id: "research_001",
  businessId: "blog-gaming",
  gameName: "Mordheim",
  topic: "New Faction Release",
  materialType: "game_update" | "patch_notes" | "community_post" | "interview",
  sourceUrl: "https://example.com/mordheim-update",
  summary: "Brief summary of research content",
  assignedTo: ["agent_researcher_1"],
  status: "pending" | "in_progress" | "completed",
  createdAt: 1711068000000,
  completedAt: null,
  articleIds: ["article_123"] // Links to articles using this research
}
```

### **3. Agent Communication Collection**
```typescript
{
  _id: "chat_001",
  businessId: "blog-gaming", // or "music"
  participants: ["Poe", "Shepherd", "Content_Agent"],
  message: "Article approved for publishing",
  timestamp: 1711068000000,
  meetingId: null, // or meeting ID if part of a meeting
  projectId: "mordheim-newsroom"
}
```

### **4. Meetings Collection**
```typescript
{
  _id: "meeting_001",
  businessId: "blog-gaming", // or "music"
  title: "Shepherd Weekly Standup",
  participants: ["Poe", "Shepherd", "Content_Agent", "Editor_Agent"],
  scheduledAt: 1711068000000,
  transcriptPath: "/data/agents/meetings/meeting_001.md",
  status: "scheduled" | "in_progress" | "completed",
  agenda: ["Review articles", "Assign research", "Publish schedule"],
  actionItems: [
    { task: "Write Mordheim article", assignee: "writer_1", due: 1711154400000 }
  ]
}
```

### **5. Projects Collection**
```typescript
{
  _id: "project_001",
  businessId: "blog-gaming", // or "music"
  name: "Mordheim Newsroom",
  owner: "Shepherd",
  status: "active",
  articles: ["article_123", "article_124"],
  research: ["research_001", "research_002"],
  meetings: ["meeting_001"],
  createdAt: 1711068000000,
  lastActivity: 1711154400000
}
```

### **6. Marketing Content Collection**
```typescript
{
  _id: "marketing_001",
  businessId: "blog-gaming", // or "music"
  platform: "twitter" | "facebook" | "instagram",
  content: "Post text",
  mediaPath: "/data/marketing/images/post_001.jpg",
  scheduledFor: 1711068000000,
  status: "draft" | "approved" | "published",
  relatedArticleId: "article_123",
  createdBy: "agent_marketing_1"
}
```

### **7. Chester Studio Collection**
```typescript
{
  _id: "song_001",
  businessId: "music",
  band: "Runefury",
  title: "Dwarf Slayer Anthem",
  lyricPath: "/data/chester/lyrics/runefury-001.md",
  audioPath: "/data/chester/audio/runefury-001.mp3",
  status: "writing" | "recording" | "mixed" | "released",
  releaseDate: null,
  tags: ["medieval", "metal", "runefury"]
}
```

---

## Multi-Gateway Setup

| Gateway | Host | Port | Purpose | Agents |
|---------|------|------|---------|--------|
| **Gateway 1** | GMKtek M6 Ultra | 8080 | Music Business | Chester, Runefury, Music Marketing |
| **Gateway 2** | GMKtek M6 Ultra | 8081 | Blog/Gaming Business | Shepherd, Content, Research, Editor, CGN Marketing |
| **Poe's Gateway** | GMKtek M6 Ultra | 8082 | Oversight | Poe (you) |

### Local Storage Structure
```
GMKtek M6 Ultra (/data/)
├── gateway-music/          # Gateway 1
│   ├── agents/
│   │   ├── chester/
│   │   ├── runefury/
│   │   └── music-marketing/
│   └── storage/
│       ├── audio/
│       └── lyrics/
├── gateway-blog/           # Gateway 2
│   ├── agents/
│   │   ├── shepherd/
│   │   ├── content/
│   │   ├── research/
│   │   ├── editor/
│   │   └── cgn-marketing/
│   └── storage/
│       ├── articles/
│       └── research/
└── gateway-poe/            # Poe's oversight
    ├── agents/
    │   └── poe/
    └── storage/
        └── oversight/
```

---

## Workflow Prevention Logic

### **Before Writer Starts Article:**
```typescript
// Query Convex for existing articles on same game + topic
const existingArticles = await query(
  "articles",
  q => q
    .withIndex("business_game_topic", 
      q => q.eq("businessId", "blog-gaming")
            .eq("gameName", "Mordheim")
            .eq("topic", "New Faction"))
    .eq("status", "published")
);

if (existingArticles.length > 0) {
  // Block writer, suggest alternative topic
  throw new Error("Article already exists. Check research materials for new angles.");
}
```

### **Before Researcher Starts Research:**
```typescript
// Query Convex for research already assigned/completed
const existingResearch = await query(
  "research",
  q => q
    .withIndex("business_game_topic", 
      q => q.eq("businessId", "blog-gaming")
            .eq("gameName", "Mordheim")
            .eq("topic", "New Faction"))
    .eq("status", "completed")
);

if (existingResearch.length > 0) {
  // Reuse existing research, assign to writer
  return existingResearch[0];
}
```

---

## Business Isolation Rules

| Component | Shared | Separate |
|-----------|--------|----------|
| Convex backend | ✓ | |
| Dashboard app | ✓ | |
| Authentication | ✓ | |
| Poe's oversight | ✓ | |
| Gateway runtime | | ✓ (3 gateways) |
| Agent sessions | | ✓ (per business) |
| Local storage | | ✓ (per business) |
| Article/Research data | | ✓ (filtered by businessId) |
| Music files | | ✓ (only music business) |
| CGN content | | ✓ (only blog business) |

### Agent Communication Rules
```typescript
// Agents can only query their own business
const articles = await query(
  "articles",
  q => q
    .withIndex("business_game_topic", 
      q => q.eq("businessId", "blog-gaming")
            .eq("gameName", "Mordheim")
            .eq("topic", "New Faction"))
);

// Cross-business queries require explicit permission
if (agent.businessId !== targetBusinessId) {
  throw new Error("Cross-business access denied");
}
```

---

## Dashboard Views

The dashboard has three tabs:

| Tab | Shows | Who Can Access |
|-----|-------|----------------|
| **Poe Overview** | Both businesses, all agents, high-level metrics | You (Ryan) only |
| **Music Studio** | Chester, Runefury, Music Marketing | Music agents + You |
| **OCG Newsroom** | Shepherd, Content, Research, Editor, OCG Marketing | OCG agents + You |

---

## Implementation Phases

### **Phase 1: Foundation (2-3 weeks)**
- [ ] Set up Convex cloud project (free tier)
- [ ] Deploy 3 OpenClaw Gateways on GMKtek (ports 8080, 8081, 8082)
- [ ] Create Convex schema files for all 7 collections
- [ ] Build Next.js dashboard frontend on Vercel (free)
- [ ] Create agent session tracking schema
- [ ] Connect Poe/Shepherd/Chester to write/read from Convex

### **Phase 2: Core Features (3-4 weeks)**
- [ ] Agent chat/communication system
- [ ] Project tracking pages
- [ ] Meeting scheduler with transcripts
- [ ] Shepherd Newsroom pipeline (research → writing → editing → publishing)
- [ ] Implement duplicate prevention logic in researcher/writer agents

### **Phase 3: Specialized Studios (4-6 weeks)**
- [ ] Chester Studio (music files, lyrics)
- [ ] Marketing Agency workspace (both businesses)
- [ ] Full visibility dashboard for Ryan
- [ ] Business isolation enforcement

### **Phase 4: Integration (2-3 weeks)**
- [ ] GMKtek local storage sync
- [ ] Mobile-responsive optimization
- [ ] Notification system
- [ ] Authentication and permissions

---

## Convex Token
```
eyJ2MiI6ImFiNDk0MjhlMDE5YTQ2NjliOWY5MDVhMThkYWQ2Nzk5In0=
```

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js (React) |
| Backend | Convex Cloud |
| Database | Convex (free tier) |
| Agent Runtime | OpenClaw Gateway (single instance) |
| File Storage | GMKtek M6 Ultra (1TB SSD) |
| Remote Access | Tailscale (optional) |
| Hosting | Vercel (free tier) |

---

## Key Decisions

- **Convex over local JSON:** Real-time sync, built-in auth, efficient queries, remote access
- **Multi-gateway architecture:** Business isolation, independent agent runtimes, Poe oversight
- **Hybrid storage:** Convex for structured data, GMKtek for large files (audio, video, markdown)
- **Duplicate prevention:** Query-by-before-write pattern with businessId + gameName + topic indexing
- **Dashboard framework:** Next.js + Convex for fastest development and best integration

---

## Open Questions

1. Should Chester and Shepherd ever need to share research (cross-business articles)?
2. What authentication method for dashboard access (Convex auth, Tailscale, custom)?
3. Should meeting transcripts be stored in Convex or GMKtek local?
4. Mobile app vs responsive web for phone/tablet access?

---

*Last Updated: 2026-03-21*
s?

---

*Last Updated: 2026-03-21*
