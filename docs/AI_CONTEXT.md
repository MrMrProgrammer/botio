I'm working on an open-source Python library called **Botio**.

Project goal:
Botio is a platform-agnostic framework for building chat bots. The main idea is that developers should be able to write their bot logic once and run it on multiple messaging platforms such as Telegram, Bale, Rubika, Eitaa, WhatsApp, Discord, and others without changing their business logic.

Core philosophy:
The bot handler should never know which platform the message came from. Platform-specific payloads must be converted into a unified internal structure through adapters.

The architecture is:

Platform Payload
→ Adapter
→ Update
→ Context
→ Dispatcher
→ Handler
→ Response
→ Adapter
→ Platform API

Current implementation:

* Language: Python
* Async-first architecture
* Published on PyPI as "botio"
* Core components:

  * BotKit (main application)
  * Adapter system
  * Dispatcher
  * Context
  * Update model
  * User model
  * Chat model
  * Message model
  * Response system

Current project structure:

botio/
├── adapters/
│   ├── base.py
│   ├── factory.py
│   ├── fake.py
│   └── telegram.py
├── app.py
├── context.py
├── dispatcher.py
├── responses.py
├── models/
│   ├── user.py
│   ├── chat.py
│   ├── message.py
│   ├── attachment.py
│   └── update.py
└── **init**.py

Important design decisions:

* Botio must not depend on FastAPI, Django, Flask, or any web framework.
* Webhook endpoints are the responsibility of the application developer.
* Botio only receives a payload through:
  await bot.process_update(platform, payload)
* Adapters are responsible for translating platform payloads into Update objects.
* Context provides helper methods such as reply() and send().
* Update is a pure data structure and contains no behavior.
* The core library should not contain platform-specific logic.
* Users should not need to instantiate TelegramAdapter directly.
* Adapters are registered through:
  bot.add(platform="telegram", token="...")

Current roadmap:

* Improve Telegram adapter
* Add command routing
* Add filters
* Add middleware system
* Add state management
* Add storage abstraction
* Add Bale adapter
* Add Rubika adapter
* Add Eitaa adapter
* Improve documentation
* Improve testing and CI/CD

When helping me:

* Focus on clean architecture.
* Keep the framework platform-agnostic.
* Avoid framework-specific coupling.
* Prefer simplicity over over-engineering.
* Design APIs similar in quality to FastAPI, Aiogram, and python-telegram-bot.
* Always consider future support for multiple messaging platforms.
* Keep backward compatibility in mind whenever possible.

Continue helping me develop Botio from its current state.
