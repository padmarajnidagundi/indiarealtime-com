"""
Telegram Bot example - Get alerts when commodities reach target price
"""

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, ConversationHandler
from indiarealtime import IndiaRealTime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

irt = IndiaRealTime()

# Conversation states
COMMODITY, TARGET_PRICE, STATE = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start the bot"""
    await update.message.reply_text(
        "🌾 Welcome to IndiaRealTime Bot!\n\n"
        "I can help you track mandi prices. Use /alert to set price alerts."
    )

async def alert_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start alert setup conversation"""
    await update.message.reply_text(
        "What commodity do you want to track?\n"
        "(e.g., wheat, rice, onion, potato)"
    )
    return COMMODITY

async def commodity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get commodity"""
    context.user_data['commodity'] = update.message.text
    await update.message.reply_text(
        f"Great! Tracking {update.message.text}.\n"
        "What's your target price (₹ per quintal)?"
    )
    return TARGET_PRICE

async def target_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get target price"""
    try:
        price = float(update.message.text)
        context.user_data['target_price'] = price
        
        # Get available states
        await update.message.reply_text(
            f"Alert when price reaches ₹{price}.\n"
            "Which state? (e.g., Punjab, Maharashtra)"
        )
        return STATE
    except ValueError:
        await update.message.reply_text("Please enter a valid price")
        return TARGET_PRICE

async def state(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Save alert and monitor"""
    context.user_data['state'] = update.message.text
    
    # Store alert in database
    alert = {
        'user_id': update.effective_user.id,
        'commodity': context.user_data['commodity'],
        'target_price': context.user_data['target_price'],
        'state': context.user_data['state'],
    }
    
    await update.message.reply_text(
        f"✓ Alert set!\n"
        f"Commodity: {alert['commodity']}\n"
        f"Target: ₹{alert['target_price']}\n"
        f"State: {alert['state']}\n\n"
        "I'll notify you when the price reaches your target."
    )
    
    # Schedule price check
    context.job_queue.run_repeating(
        check_price,
        interval=3600,  # Check every hour
        first=60,
        data={'user_id': update.effective_user.id, 'alert': alert},
    )
    
    return ConversationHandler.END

async def check_price(context: ContextTypes.DEFAULT_TYPE):
    """Check price and notify if target reached"""
    data = context.job.data
    alert = data['alert']
    
    try:
        prices = irt.mandi_prices(
            commodity=alert['commodity'],
            state=alert['state']
        )
        
        if prices:
            current_price = prices[0].price
            if current_price <= alert['target_price']:
                await context.bot.send_message(
                    chat_id=data['user_id'],
                    text=f"🎉 Alert! {alert['commodity'].upper()} reached your target!\n\n"
                         f"Current price: ₹{current_price}\n"
                         f"Your target: ₹{alert['target_price']}\n"
                         f"Market: {prices[0].market}\n"
                         f"Updated: {prices[0].updated_at}"
                )
                # Remove this job after alert
                context.job.schedule_removal()
    except Exception as e:
        logger.error(f"Error checking price: {e}")

async def aqi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get AQI for a city"""
    if not context.args:
        await update.message.reply_text("Usage: /aqi <city_name>")
        return
    
    city = " ".join(context.args)
    try:
        results = irt.air_quality(city=city)
        if results:
            r = results[0]
            emoji = "🟢" if r.aqi <= 50 else "🟡" if r.aqi <= 100 else "🔴"
            await update.message.reply_text(
                f"{emoji} Air Quality in {city}\n\n"
                f"AQI: {r.aqi} ({r.aqi_category})\n"
                f"PM2.5: {r.pm25:.0f} µg/m³\n"
                f"PM10: {r.pm10:.0f} µg/m³"
            )
        else:
            await update.message.reply_text(f"No AQI data found for {city}")
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancel conversation"""
    await update.message.reply_text("Cancelled.")
    return ConversationHandler.END

def main():
    """Start the bot"""
    # Replace with your bot token
    application = Application.builder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("aqi", aqi_command))
    
    # Alert conversation
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("alert", alert_start)],
        states={
            COMMODITY: [CommandHandler("text", commodity)],
            TARGET_PRICE: [CommandHandler("text", target_price)],
            STATE: [CommandHandler("text", state)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)
    
    # Start bot
    application.run_polling()

if __name__ == '__main__':
    main()
