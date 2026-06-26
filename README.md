# Botio

Botio is a platform-agnostic framework for building chat bots.

The goal of Botio is simple: **write your bot logic once and run it on multiple messaging platforms** without rewriting your handlers for each platform.

## Why Botio?

Building bots for different platforms is often repetitive.

Every platform has its own:

* Update structure
* User model
* Message format
* Webhook payload
* API methods

As a result, developers usually end up maintaining separate codebases for Telegram, Bale, Rubika, Eitaa, and other platforms.

Botio solves this problem by introducing a unified abstraction layer.

Instead of writing platform-specific code, you write your business logic against a common interface.

## Philosophy

Your bot should not care where a message came from.

This:

```python
if platform == "telegram":
    ...
elif platform == "rubika":
    ...
elif platform == "bale":
    ...
```

should not exist inside your handlers.

Instead, Botio normalizes incoming updates into a unified structure.

```text
Platform Payload
        ↓
Adapter
        ↓
Update
        ↓
Context
        ↓
Handler
        ↓
Response
        ↓
Adapter
        ↓
Platform API
```

Your handlers receive a platform-independent context and can focus entirely on business logic.

## Features

* Platform-independent bot architecture
* Unified Update model
* Unified User, Chat and Message models
* Adapter-based design
* Async-first architecture
* Extensible platform support
* Framework agnostic
* Simple handler registration

## Current Status

Botio is currently in its early stages of development.

The project is focused on building a clean foundation that can support multiple messaging platforms through adapters.

Supported and planned platforms include:

* Telegram
* Bale
* Rubika
* Eitaa
* WhatsApp
* Discord
* Custom adapters

## Installation

```bash
pip install botio
```

## Quick Start

```python
from botio import BotKit

bot = BotKit()

bot.add(
    platform="telegram",
    token="YOUR_TOKEN",
)

@bot.message
async def echo(ctx):
    await ctx.reply(
        ctx.message.text
    )
```

## Core Concepts

### Update

A normalized representation of an incoming event.

### Context

Provides access to the update and helper methods such as replying to messages.

### Adapter

Responsible for translating platform-specific payloads into Botio updates and converting Botio responses back into platform API calls.

### Dispatcher

Routes updates to the appropriate handlers.

## Design Goals

* Keep business logic platform independent
* Hide platform-specific complexity
* Keep the core lightweight
* Avoid framework lock-in
* Make adapters easy to build
* Provide a consistent developer experience

## Roadmap

* [x] Core architecture
* [x] Adapter system
* [x] Telegram adapter (MVP)
* [ ] Command handlers
* [ ] Middleware system
* [ ] Filters
* [ ] State management
* [ ] Storage backends
* [ ] Bale adapter
* [ ] Rubika adapter
* [ ] Eitaa adapter
* [ ] Webhook utilities

## Contributing

Contributions, ideas, bug reports, and pull requests are welcome.

## License

MIT
