# 🎥 YouTube Downloader Telegram Bot

A Telegram bot built with Python that lets users download YouTube videos, audio, and thumbnails directly from Telegram. Users can either send a YouTube URL or search by video title, then choose what they want to download.

The bot supports downloading audio (MP3), video, and thumbnails through an interactive inline keyboard.

---

## Features

- 🎵 Download YouTube audio
- 🎬 Download YouTube videos
- 🖼️ Download video thumbnails
- 🔎 Search YouTube by title
- 🔗 Accept direct YouTube URLs
- 🤖 Interactive Telegram interface
- 📱 Inline keyboard for download options
- ⚡ Automatic cleanup of downloaded files

---

## Tech Stack

- Python
- Pyrogram
- pytube
- youtube-search
- pyLense
- PyMongo
- convopyro

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sigmaCoderx/youtube-downloader.git
cd youtube-downloader
```

### Create a virtual environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Before running the bot, replace the placeholders in the source code.

### Telegram Bot Token

```python
BotTokn = "YOUR_BOT_TOKEN"
```

Create one using:

https://t.me/BotFather

---

### Telegram API Credentials

Create an application at:

https://my.telegram.org

Replace:

```python
apiID = YOUR_API_ID
apiHash = "YOUR_API_HASH"
```

---

### MongoDB (Optional)

The project includes MongoDB support for future features.

Replace:

```python
<MONGODB_URL>
```

with your database connection string if you plan to use it.

---

## Running the Bot

```bash
python pyroYoutubeDownloader.py
```

---

## How It Works

1. Start the bot with `/start`.
2. Send a YouTube URL or search query.
3. The bot displays download options.
4. Choose one of:

- 🎵 Audio
- 🎬 Video
- 🖼️ Thumbnail

5. The requested media is downloaded and sent directly in Telegram.

---

## Example

### Input

```
https://youtu.be/dQw4w9WgXcQ
```

or

```
Alan Walker Faded
```

### Output

```
Choose one:

🎵 Audio
🎬 Video
🖼️ Thumbnail
```

---

## Project Structure

```
youtube-downloader/
├── pyroYoutubeDownloader.py
├── requirements.txt
└── README.md
```

---

## Requirements

All project dependencies are listed in **requirements.txt**.

Install them with:

```bash
pip install -r requirements.txt
```

---

## Notes

- Requires a Telegram Bot Token.
- Requires Telegram API ID and API Hash.
- Requires an active internet connection.
- Downloaded files are automatically removed after being sent.
- Some YouTube videos may not be downloadable due to age restrictions, private status, or regional limitations.
- Never commit your Bot Token or API credentials to GitHub.

---

## Future Improvements

- Playlist downloads
- Multiple quality options
- Progress indicator
- Download queue
- User history
- Admin dashboard
- Better error handling

---

## License

MIT License

---

## Author

**flippedCoin**

GitHub: https://github.com/sigmaCoderx

---

⭐ If you found this project useful, consider giving it a star on GitHub.
