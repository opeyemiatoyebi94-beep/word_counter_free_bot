# Word Counter Bot

A Telegram bot that counts words, characters, sentences, and paragraphs in any text you send it.

## 1. Create the bot on Telegram

1. Open Telegram and message **@BotFather**
2. Send `/newbot`
3. Give it a display name (e.g., "Word Counter")
4. Give it the username `word_counter_free_bot` (or another available name)
5. BotFather will give you a **token** — copy it, you'll need it below. Keep it secret!

## 2. Push this project to GitHub

From this folder:

```bash
git init
git add .
git commit -m "Initial commit: word counter bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/word-counter-bot.git
git push -u origin main
```

(Create an empty repo first on github.com named `word-counter-bot`, without a README, so there's no conflict.)

## 3. Deploy on Railway

1. Go to [railway.app](https://railway.app) and log in (GitHub login is easiest)
2. Click **New Project** → **Deploy from GitHub repo**
3. Select your `word-counter-bot` repo
4. Railway will detect the `Procfile` and `requirements.txt` automatically
5. Go to your service's **Variables** tab and add:
   - `BOT_TOKEN` = the token BotFather gave you
6. Railway will build and deploy automatically. Check the **Deployments → Logs** tab — you should see `Bot starting...`

## 4. Test it

Open Telegram, search for `@word_counter_free_bot`, hit **Start**, and send it some text. It should reply with word/character/sentence/paragraph counts.

## Notes

- Never commit your bot token to GitHub. It's read from the `BOT_TOKEN` environment variable, set only in Railway.
- If you rotate/regenerate the token in BotFather, just update the Railway variable — no code changes needed.
- Railway's free tier has usage limits; check current pricing at railway.app/pricing.
