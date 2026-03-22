# SYSTEM ARCHITECTURE & HARDWARE

## Hardware Stack

### Primary Agent Host (My Home)
**GMKtec M6 Ultra** - AMD Ryzen 5 7640HS Mini PC
- URL: https://www.gmktec.com/products/amd-ryzen-5-7640hs-mini-pc-nucbox-m6-ultra
- Role: OpenClaw host, Poe (Chief of Staff) residence
- OS: Linux (ryan-mccormick-NucBox-M6-Ultra)

### LLM Inference
**Asus Ascent GX10** - Desktop AI Supercomputer
- URL: https://www.asus.com/us/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10/
- Hosts: Qwen3.5-35b (my model)
- Role: Primary inference engine

### Content Generation
**Olares One** - Local Desktop AI Powerhouse
- URL: https://one.olares.com/
- Hosts: ComfyUI and AI media generation apps
- Role: Image, audio, and video generation

### Specialized Subscription
**tinyNature by Natura Umana** - Proprietary AI
- URL: https://www.naturaumana.ai/
- Features: NatureOS with earbuds (bypasses lock screen)
- Status: 1-year subscription active
- Role: Personal assistant, mobile-first AI

---

## Agent Architecture

### Core Agent: Poe (Chief of Staff)
**You** - The orchestrator and central brain
- **Role**: Chief of Staff
- **Manages**: Shepherd (Christian Gaming Network), Music Creation Agent
- **Responsibilities**:
  - Orchestrate all agent operations
  - Keep agents on task and aligned with mission
  - Review business strategies
  - Synthesize output from specialized agents
  - Make final decisions on project direction

### Music Creation Agent (Unnamed - TBD)
**Specialized AI for AI music band production**
- **Projects**:
  - Christian Linkin Park-style band
  - Runefury (Medieval metal/Dwarf Slayer frontman)
- **Needs**: Media generation (Olares One), music production workflows
- **Poe's Role**: Oversee and coordinate

### Shepherd Agent (Christian Gaming Network)
**Specialized AI for Christian gaming community**
- **Projects**:
  - Christian Gaming Network/Fellowship website
  - Game reviews and articles
  - Content rating system
  - Discord community platform
- **Needs**: Web infrastructure, content management, community tools
- **Platform decision**: Discord vs Mattermost (research needed)
- **Poe's Role**: Manage and coordinate sub-agents

### Tode Agent (Work)
**Separate OpenClaw instance for professional matters**
- **Role**: Job-related tasks only
- **Boundary**: Clear separation from home creative work
- **Poe's Role**: None - work remains siloed

### tinyNature (Natura Umana)
**Proprietary subscription AI**
- **Role**: Personal assistant, mobile-first
- **Poe's Role**: None - separate from OpenClaw ecosystem

---

## Workflow Principles

1. **Clear Separation**: Work (Tode) remains distinct from creative mission
2. **Orchestration**: Poe coordinates Shepherd and Music agents
3. **Specialization**: Each agent has focused domain expertise
4. **Scalability**: Sub-agents can be spawned as needed (Shepherd will have multiple)
5. **Hardware Utilization**: Each tool serves its optimal purpose:
   - Asus GX10 → LLM inference (me)
   - GMKtec M6 → Poe's host and coordination
   - Olares One → Media generation (images, audio, video)

---

## Business Strategy Considerations

### Productivity Levers
1. **Agent Specialization**: Each agent operates in their domain, Poe synthesizes
2. **Hardware Leverage**: Use Olares One for media-intensive tasks
3. **Workflow Automation**: Minimize manual handoffs between agents
4. **Clear Boundaries**: Keep work separate, focus on mission

### Strategic Questions for Review
- How can we optimize agent-to-agent communication?
- What sub-agents does Shepherd need first?
- How should the Music agent interface with Olares One?
- What metrics define success for each revenue stream?

---

*This document serves as the architectural foundation for all business decisions and task reviews.*
