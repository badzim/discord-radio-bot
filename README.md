# Discord Radio Bot

A Discord bot that plays YouTube playlists as a radio in voice channels.

## Features

- **Play YouTube Playlists**: Join a voice channel and play a YouTube playlist as a continuous stream of music.
- **Simple Commands**: Control the bot with simple commands like `!play` and `!stop`.
- **Automatic Disconnect**: The bot will automatically disconnect if it's the last one in the channel.

## Getting Started

### Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system. Check your version with:
  ```bash
  python3 --version
  ```
- **Git**: Required to clone the repository.

- **ffmpeg**: Required in the host machine to decode audio format to audio stream

### Installation

1. **Clone the Repository**:

   Clone the project to your local machine:

   ```bash
   git clone git@github.com:ton-utilisateur/discord-radio-bot.git
   cd discord-radio-bot
   ```

2. **Create a Virtual Environment**:

   Set up a virtual environment to manage dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the Required Dependencies**:

   Install the necessary Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Environment Variables**:

   Copy the `.env.example` file to `.env` and update it with your Discord bot token:

   ```bash
   cp .env.example .env
   ```

   Open `.env` in a text editor and replace `your_token_here` with your actual Discord bot token:

   ```bash
   DISCORD_TOKEN=your_token_here
   ```

### Usage

1. **Run the Bot**:

   After setting up the environment and dependencies, you can start the bot with:

   ```bash
   python bot.py
   ```

2. **Bot Commands**:

   - **`!play <YouTube Playlist URL>`**: The bot joins your voice channel and starts playing the playlist.
   - **`!stop`**: Stops the music and disconnects the bot from the voice channel.

### Project Structure

Here's a brief overview of the project's structure:

```
discord-radio-bot/
├── bot.py                 # Main bot script
├── requirements.txt       # List of Python dependencies
├── .env.example           # Example environment configuration
├── README.md              # Project documentation
└── venv/                  # Python virtual environment (not included in the repository)
```

### Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thanks to the [discord.py](https://github.com/Rapptz/discord.py) community for their amazing library.
- Inspiration from various Discord bot projects available online.


### Explications Complémentaires :

1. **Features** : Cette section décrit les fonctionnalités principales du bot.
2. **Getting Started** : Explique comment configurer l'environnement pour développer ou utiliser le bot, y compris les prérequis, l'installation et la configuration des variables d'environnement.
3. **Usage** : Fournit des instructions sur la manière d'utiliser le bot une fois qu'il est configuré.
4. **Project Structure** : Offre une vue d'ensemble de la structure du projet pour aider les contributeurs à s'orienter rapidement.
5. **Contributing** : Décrit le processus pour contribuer au projet.
6. **License** : Informe les utilisateurs sur les conditions de licence du projet.
7. **Acknowledgments** : Remercie les ressources et les personnes qui ont inspiré ou contribué à ce projet.

Ce README devrait te permettre de documenter ton projet de manière claire et accessible pour toi-même et pour d'éventuels contributeurs.